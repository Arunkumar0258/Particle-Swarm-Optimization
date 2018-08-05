import numpy as np
from matplotlib.pyplot import subplots

def f(x):
    return x*(x-8)

particles = 30

positions = np.random.uniform(-10, 10, particles)
velocities = np.random.uniform(-10, 10, particles)
positions_best = positions
num_iters = 500

w = 0.1
c1 = 0.01
c2 = 0.01

gbest = 0

for i in range(particles):
    if(f(positions[i]) < f(gbest)):
        gbest = positions[i]

fig, ax = subplots()
fig.show()

for _ in range(num_iters):
    for i in range(particles):
        velocities[i] = w*velocities[i] + c1*np.random.uniform(0,1,1)*(positions_best[i] - positions[i])
        + c2*np.random.uniform(0,1,1)*(gbest - positions[i])

        positions[i] += velocities[i]

        if(f(positions[i]) < f(positions_best[i])):
            positions_best[i] = positions[i]

            if(f(positions_best[i]) < f(gbest)):
                gbest = positions_best[i]
        
        ax.clear()
        ax.axis([-20, 20, -20, 20])
        ax.plot(np.arange(-10, 10, 0.1), f(np.arange(-10, 10, 0.1)), '-')
        ax.plot(positions, f(positions), 'ro', markersize = 5)

        fig.canvas.draw()




