import numpy as np
import matplotlib.pyplot as plt

# Basic orbit simulation (circular around sun)
theta = np.linspace(0, 2*np.pi, 100)  # Angles
radius = 1  # AU for Earth
x = radius * np.cos(theta)
y = radius * np.sin(theta)

plt.plot(x, y)
plt.title("Earth's Orbit Around the Sun")
plt.xlabel("X (AU)")
plt.ylabel("Y (AU)")
plt.axis('equal')
plt.show()