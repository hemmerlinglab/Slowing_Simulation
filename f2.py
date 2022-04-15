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


laser_detuning = 120.0 #+ -v_max_Boffset # in m/s


# end of simulation, i.e. position of the MOT or a wall
s_max = 0.7

slowing_time = 5.0e-3

L_start = 0.1
Zeeman_length = 0.2
gF = 2.0
v_max = 400.0

linewidth = 10.0e6
gamma1 = 2*np.pi * linewidth
#omega = 0.25 * gamma1 

s0 = 0.25

sx_noslow = np.copy(sx)
vx_noslow = np.copy(vx)



my_title = 'Yb Slowing'


