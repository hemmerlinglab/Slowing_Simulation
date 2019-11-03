# load initial conditions for particles

no_of_particles = 100

skip_points = 100

dt = 1e-6
tsteps = np.int(60e-3/dt)


sx = np.zeros([no_of_particles, tsteps])
vx = np.zeros([no_of_particles, tsteps])

#for k in range(no_of_particles):
#    vx[k, 0] = 100.0 + (200.0) * np.float(k)/no_of_particles

vx[:, 0] = np.random.normal(250.0, 50.0, no_of_particles)

# shifting particles to negative positions, same as starting at later times
sx[:, 0] = np.random.normal(-50.0e-3, 50.0e-3, no_of_particles)

laser_detuning = 0.0 # in m/s

slowing_time = 5.0e-3

L_start = 0.1
Zeeman_length = 0.2
gF = 2.0
v_max = 400.0

linewidth = 30.0e6
gamma1 = 2*np.pi * linewidth
omega = 0.09225 * gamma1 

sx_noslow = np.copy(sx)
vx_noslow = np.copy(vx)

