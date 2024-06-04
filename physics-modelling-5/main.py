import numpy as np
import matplotlib.pyplot as plt


def calculate_intensity(phi, slit_width, slit_separation, wavelength, num_slits):
    return (np.sin(np.pi * slit_width / wavelength * np.sin(phi)) /
            (np.sin(phi) * np.pi * slit_width / wavelength)) ** 2 * \
        (np.sin(num_slits * np.pi * slit_separation / wavelength * np.sin(phi)) /
         np.sin(np.sin(phi) * np.pi * slit_separation / wavelength)) ** 2


num_slits = 10
slit_width = 100
slit_separation = 200
wavelength = 0.64
factor = 2

delta_lambda = wavelength / (num_slits * factor)
lambda2 = wavelength + delta_lambda

phi = np.linspace(-np.pi, np.pi, 1000000)

intensity1 = calculate_intensity(phi, slit_width, slit_separation, wavelength, num_slits)
intensity2 = calculate_intensity(phi, slit_width, slit_separation, lambda2, num_slits)

plt.figure(figsize=(10, 6))
plt.plot(phi, intensity1, label=f'Intensity for λ = {wavelength:.2f} μm')
plt.plot(phi, intensity2, label=f'Intensity for λ = {lambda2:.2f} μm')
plt.xlim(-0.02, 0.02)
plt.ylim(0, num_slits ** 2 / 2)
plt.xlabel(r'$\varphi$, rad')
plt.ylabel(r'Intensity')
plt.legend()
plt.show()
