# load initial conditions for particles

no_of_particles = 100

skip_points = 100

dt = 1e-6
tsteps = np.int(60e-3/dt)


tx = np.zeros([no_of_particles, tsteps])
sx = np.zeros([no_of_particles, tsteps])
vx = np.zeros([no_of_particles, tsteps])


# starting positions
sx[:, 0] = 0.0 #np.random.normal(-50.0e-3, 50.0e-3, no_of_particles)

# initial velocities
vx[:, 0] = np.random.normal(500.0, 5.0, no_of_particles)

# initial times
tx[:, 0] = np.random.poisson(1.0, no_of_particles) * 1e-4
#tx[:, 0] = np.random.normal(0.5e-3, 2.5e-3, no_of_particles)


v_max_B0 = 500.0
v_max_Boffset = -v_max_B0/2.0


laser_detuning = 10.0 + -v_max_Boffset # in m/s



slowing_time = 10.0e-3

L_start = 0.1
Zeeman_length = 0.2
gF = 2.0
v_max = 400.0

linewidth = 30.0e6
gamma1 = 2*np.pi * linewidth
omega = 0.09225 * gamma1 

sx_noslow = np.copy(sx)
vx_noslow = np.copy(vx)




