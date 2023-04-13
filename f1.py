# load initial conditions for particles

no_of_particles = 500

skip_points = 100

dt = 1e-6
tsteps = np.int64(60e-3/dt)


tx = np.zeros([no_of_particles, tsteps])
sx = np.zeros([no_of_particles, tsteps])
vx = np.zeros([no_of_particles, tsteps])


# starting positions
sx[:, 0] = 0.0 #np.random.normal(-50.0e-3, 50.0e-3, no_of_particles)

# initial velocities
vx[0:int(no_of_particles/2), 0] = np.random.normal(120.0, 15.0, int(no_of_particles/2))
vx[int(no_of_particles/2):, 0] = np.random.normal(120.0, 15.0, int(no_of_particles/2))

# initial times
tx[:, 0] = np.random.poisson(1.0, no_of_particles) * 1e-4
#tx[:, 0] = np.random.normal(0.5e-3, 2.5e-3, no_of_particles)


use_zeeman_slower = False

v_max_B0 = 500.0
v_max_Boffset = -v_max_B0/2.0


# end of simulation, i.e. position of the MOT or a wall
s_max = 0.8



L_start = 0.1
Zeeman_length = 0.2
gF = 2.0
v_max = 400.0

linewidth = 28.0e6
gamma1 = 2*np.pi * linewidth
#omega = 0.25 * gamma1 



# slowing laser
slowing_time = 8.0e-3
s0 = (20 / (np.pi*(0.5)**2)) / 63 # 63 mW/cm^2
laser_detuning = 100.0 # in m/s


# mot laser
use_mot_laser = True
s0_mot = (2*10 / (np.pi*(0.5)**2)) / 63 # 63 mW/cm^2
mot_position = 0.7
mot_width = 1e-2
mot_laser_detuning = 5.0 # m/s



sx_noslow = np.copy(sx)
vx_noslow = np.copy(vx)



my_title = 'Yb Slowing'


