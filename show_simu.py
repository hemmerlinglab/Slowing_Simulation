import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sys
import pickle


save_file = sys.argv[1] + '_results.dat'

p_out = open(save_file, 'rb')
arr = pickle.load(p_out)
p_out.close()

for k in arr.keys():
    # define all variables saved in arr as variables
    print(k + ' = arr["' + k + '"]')
    exec(k + ' = arr["' + k + '"]')



def bin_data(no_of_particles, x, t, v, det_pos):

    t_arr = np.linspace(0,30,120) * 1e-3
    v_arr = np.linspace(0,700,100)

    result = np.zeros([len(v_arr)+1, len(t_arr)+1])


    # toggle through all particles and check if they arrived at the detection region
    for n in range(no_of_particles):
        
        ind = np.where( np.abs(x[n, :] - det_pos) < 3e-3 )[0]
        if len(ind)>0:
            # particle reached detector
            ind = ind[0]
            vdet_ind = np.digitize(v[n, ind], v_arr)
            tdet_ind = np.digitize(t[ind], t_arr)

            result[vdet_ind, tdet_ind] += 1

    return (t_arr, v_arr, result[:-2, :-2])

        

det_pos = 0.8 # in m


# some plotting
vi = vx[:, 0]

plt.figure(figsize = (12,12))

for k in range(no_of_particles):
    plt.subplot(3,3,1)
    plt.plot(ts * 1e3, sx[k, :])

plt.xlabel('Time (ms)')
plt.ylabel('Position (m)')
plt.tight_layout()

for k in range(no_of_particles):
    plt.subplot(3,3,2)
    plt.plot(ts * 1e3, vx[k, :])

plt.xlabel('Time (ms)')
plt.ylabel('Velocity (m/s)')
plt.tight_layout()

plt.axvline(slowing_time * 1e3, ls='--')



for k in range(no_of_particles):
    plt.subplot(3,3,3)
    plt.plot(sx[k, :], vx[k, :])

plt.xlabel('Position (m)')
plt.ylabel('Velocity (m/s)')

plt.axvline(L_start, ls='--')
plt.axvline(L_start + Zeeman_length, ls='--')

plt.text(0.8, 300.0, 'B0 = ' + str(B0))

plt.tight_layout()


vi = vx[:, 0]
vf = vx[:, -1]
vf_noslow= vx_noslow[:, -1]

sort_ind = np.argsort(vi)
vi = vi[sort_ind]
vf = vf[sort_ind]
vf_noslow = vf_noslow[sort_ind]


plt.subplot(3,3,4)
plt.plot(vi, vf)
plt.plot(vi, vi, 'r--', lw = 0.25)
plt.axhline(laser_detuning, ls='--') # detuning is in m/s

plt.xlabel('Initial velocity (m/s)')
plt.ylabel('Final velocity (m/s)')

plt.tight_layout()

plt.subplot(3,3,7)

plt.hist(tx[:, 0] * 1e3, bins = no_of_particles)
plt.xlabel('Initial times (ms)')
plt.tight_layout()

plt.subplot(3,3,8)

plt.hist(sx[:, 0] * 1e3, bins = no_of_particles)
plt.xlabel('Initial position (mm)')
plt.tight_layout()

plt.subplot(3,3,9)

plt.hist(vi, bins = no_of_particles)
plt.xlabel('Initial velocities (m/s)')
plt.tight_layout()



cmax = 5.0

plt.figure(figsize=(10,10))

(t_arr, v_arr, result_noslow) = bin_data(no_of_particles, sx_noslow, ts, vx_noslow, det_pos)

plt.subplot(2,2,1)
plt.pcolor(t_arr * 1e3, v_arr, result_noslow)

plt.plot(t_arr * 1e3, det_pos/t_arr, 'r--', lw = 0.25)
plt.xlabel('Time (ms)')
plt.ylabel('Velocities (m/s)')
plt.ylim(np.min(v_arr), np.max(v_arr))
plt.clim(0, cmax)
plt.colorbar()
plt.tight_layout()

(t_arr, v_arr, result) = bin_data(no_of_particles, sx, ts, vx, det_pos)

plt.subplot(2,2,2)
plt.pcolor(t_arr * 1e3, v_arr, result)
plt.plot(t_arr * 1e3, det_pos/t_arr, 'r--', lw = 0.25)
plt.xlabel('Time (ms)')
plt.ylabel('Velocities (m/s)')
plt.ylim(np.min(v_arr), np.max(v_arr))
plt.clim(0, cmax)
plt.colorbar()
plt.tight_layout()

print(np.sum(np.sum(result_noslow)))
print(np.sum(np.sum(result)))


plt.subplot(2,2,3)
plt.plot( t_arr[:-1] * 1e3, np.sum(result, axis = 0) )
plt.plot( t_arr[:-1] * 1e3, np.sum(result_noslow, axis = 0) )
plt.tight_layout()

plt.subplot(2,2,4)
plt.plot( v_arr[:-1], np.sum(result, axis = 1) )
plt.plot( v_arr[:-1], np.sum(result_noslow, axis = 1) )
plt.tight_layout()

plt.show()




