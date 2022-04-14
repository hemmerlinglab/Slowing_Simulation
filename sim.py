import numpy as np
#import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
import sys
import pickle

# constants

kB = 1.38064e-23
e_charge = 1.6e-19
epsilon_0 = 8.854e-12
k_e = 1/(4.0 * np.pi * epsilon_0)
amu = 1.6605e-27
hbar = 6.62607e-34/2.0/np.pi
muB = 9.274e-24


lambda_yb = 398.0e-9
k_vec = 2*np.pi/lambda_yb



mass = 174 * amu





### functions ######################################

def save_to_arr(str_list):

    arr = {}
    for s in str_list:
        exec('arr["' + s + '"] = ' + s)

    return arr




### main ######################################

# get initial conditions for all particles
filename = sys.argv[1] + '.py'

exec(open(filename).read(), globals())

# get number of particles
no_of_particles = sx.shape[0]

# mask array to check if simulation should stop for particle
do_simu = np.ones(no_of_particles, dtype = bool)
part_arr = np.array(np.linspace(0,no_of_particles-1, no_of_particles), dtype = np.int64)


# sx[m, k] : m = particle number, k = time step

ts = np.array([0])

for k in range(tsteps-1):

    if k % int(tsteps/1000.0) == 0:
        print(str(k) + " of " + str(tsteps) + " total; simulating " + str(np.sum(do_simu)) + '/' + str(no_of_particles) + ' particles', end = "\r", flush = True)

    for n in part_arr[do_simu]:

        if tx[n, 0] <= ts[-1]:
            # only start propagating if particle is emitted from cell already

            s0 = 2.0*omega/gamma1 # check

            # single laser detuning
            # detuning = k_vec * (vx[n, k] - laser_detuning)
            
            # Zeeman slower: dE = muB * gF * B == hbar * k * v_max
            # B0 = hbar * k * v_max/ (muB * gF)
            # B(x) = Bg + B0 * sqrt(1 - x^2/L0^2)

            if (use_zeeman_slower) and (sx[n, k] > L_start) and (sx[n, k] < L_start + Zeeman_length):
                detuning = k_vec * (vx[n, k] - laser_detuning - v_max_Boffset - v_max_B0 * np.sqrt(1 - (sx[n, k] - L_start)/Zeeman_length))
            else:
                detuning = k_vec * (vx[n, k] - laser_detuning)
            
            force = -hbar * k_vec * gamma1 * s0/(1.0+s0+4.0*(detuning/gamma1)**2)

            # F = hbar * k * Gamma_eff * dt
            # F = m * dv/dt -> dv = F/m * dt + laser in -x direction
            
            # propagate particle

            # if particle is out of the cell and the slowing laser is still on, apply laser force
            if (ts[-1] <= slowing_time) and (sx[n, k] >= 0.0):
            #if (sx[n, k] >= 0.0):
                dvx = force/mass * dt
            else:
                dvx = 0.0

            vx[n, k+1] = vx[n, k] + dvx
            sx[n, k+1] = sx[n, k] + vx[n, k+1] * dt

            vx_noslow[n, k+1] = vx_noslow[n, k]
            sx_noslow[n, k+1] = sx_noslow[n, k] + vx_noslow[n, k+1] * dt


            # if particle hits the wall or if particle turns around, stop simulation
            if (sx[n, k+1] >= 1.0) or (vx[n, k+1] <= 0.0):
                do_simu[n] = False
                sx[n, k+1:] = 1.0
                vx[n, k+1:] = vx[n, k+1]

            if sx_noslow[n, k+1] >= 1.0:
                sx_noslow[n, k+1:] = 1.0
                vx_noslow[n, k+1:] = vx_noslow[n, k+1]


        else:
            # particle hasn't been emitted yet
            vx[n, k+1] = vx[n, k]
            sx[n, k+1] = sx[n, k]

            vx_noslow[n, k+1] = vx_noslow[n, k]
            sx_noslow[n, k+1] = sx_noslow[n, k]
            


    ts = np.append(ts, ts[-1] + dt)
    tx[:, k+1] = ts[-1]


# shorten arrays
ts = ts[0::skip_points]
tx = tx[:, 0::skip_points]
sx = sx[:, 0::skip_points]
vx = vx[:, 0::skip_points]
sx_noslow = sx_noslow[:, 0::skip_points]
vx_noslow = vx_noslow[:, 0::skip_points]



B0 = hbar * k_vec * v_max_B0 / (muB * gF)
Boffset = hbar * k_vec * v_max_Boffset / (muB * gF)


f = open(filename,'r')

arr = {}

arr = save_to_arr(['no_of_particles', 'dt','laser_detuning','L_start', 'Zeeman_length', 'slowing_time','ts','tx','sx','vx','sx_noslow','vx_noslow', 'B0', 'Boffset'])

arr['init_file'] = f.readlines()

f.close()

# save to file

save_file = sys.argv[1] + '_results.dat'

p_out = open(save_file, 'wb')
pickle.dump(arr, p_out)
p_out.close()

print()
print()

