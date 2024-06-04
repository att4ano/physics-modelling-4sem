import numpy as np
import matplotlib.pyplot as plt

wavelength = 500
thickness = 10000
speed_of_light = 3 * 10**8
omega = 2 * np.pi * speed_of_light / (wavelength * 1e-9)
angle = np.pi / 3

n_e = np.sqrt(1 + 2.9804 / (1 - 0.02047 / (wavelength**2)) + 0.5981 / (1 - 0.0666 / (wavelength**2)) + 8.9543 / (1 - 416.08 / (wavelength**2)))
n_o = np.sqrt(1 + 2.6734 / (1 - 0.01764 / (wavelength**2)) + 1.2290 / (1 - 0.05914 / (wavelength**2)) + 12.614 / (1 - 474.60 / (wavelength**2)))

phi_e = 2 * np.pi / wavelength * thickness * n_e
phi_o = 2 * np.pi / wavelength * thickness * n_o

time = np.linspace(0, 2 * np.pi / omega, 10000)

E0x = np.cos(angle) * np.sin(omega * time)
E0y = np.sin(angle) * np.sin(omega * time)
E1 = np.cos(angle) * np.sin(omega * time - phi_e)
E2 = np.sin(angle) * np.sin(omega * time - phi_o)

plt.figure()
plt.plot(E1, E2, label='Modified Electric Field')
plt.plot(E0x, E0y, 'r', label='Original Electric Field')
plt.xlabel('E1')
plt.ylabel('E2')
plt.legend()
plt.grid(True)
plt.show()
