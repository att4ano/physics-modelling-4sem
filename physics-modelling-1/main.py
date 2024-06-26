import numpy as np
import matplotlib.pyplot as plt


def calculate_intensity(phi, slit_width, slit_separation, wavelength, num_slits):
    return (np.sin(np.pi * slit_width / wavelength * np.sin(phi)) /
            (np.sin(phi) * np.pi * slit_width / wavelength)) ** 2 * \
        (np.sin(num_slits * np.pi * slit_separation / wavelength * np.sin(phi)) /
         np.sin(np.sin(phi) * np.pi * slit_separation / wavelength)) ** 2


def wavelength_to_rgb(wavelength):
    gamma = 0.8
    intensity_max = 255
    factor = 0.0
    R = G = B = 0

    if 380 <= wavelength <= 440:
        R = -(wavelength - 440) / (440 - 380)
        G = 0.0
        B = 1.0
    elif 440 <= wavelength <= 490:
        R = 0.0
        G = (wavelength - 440) / (490 - 440)
        B = 1.0
    elif 490 <= wavelength <= 510:
        R = 0.0
        G = 1.0
        B = -(wavelength - 510) / (510 - 490)
    elif 510 <= wavelength <= 580:
        R = (wavelength - 510) / (580 - 510)
        G = 1.0
        B = 0.0
    elif 580 <= wavelength <= 645:
        R = 1.0
        G = -(wavelength - 645) / (645 - 580)
        B = 0.0
    elif 645 <= wavelength <= 780:
        R = 1.0
        G = 0.0
        B = 0.0

    if 380 <= wavelength <= 420:
        factor = 0.3 + 0.7 * (wavelength - 380) / (420 - 380)
    elif 420 <= wavelength <= 645:
        factor = 1.0
    elif 645 <= wavelength <= 780:
        factor = 0.3 + 0.7 * (780 - wavelength) / (780 - 645)

    R = int(intensity_max * ((R * factor) ** gamma))
    G = int(intensity_max * ((G * factor) ** gamma))
    B = int(intensity_max * ((B * factor) ** gamma))

    return R, G, B


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

tmp_intensity1 = calculate_intensity(-np.pi, slit_width, slit_separation, wavelength, num_slits)
tmp_intensity2 = calculate_intensity(np.pi, slit_width, slit_separation, wavelength, num_slits)

plt.figure(figsize=(10, 6))

plt.plot(phi, intensity1, label=f'Intensity for λ = {wavelength:.2f} μm')
plt.plot(phi, intensity2, label=f'Intensity for λ = {lambda2:.2f} μm')
plt.xlim(-0.02, 0.02)
plt.ylim(0, num_slits ** 2 / 2)
plt.xlabel(r'$\varphi$, rad')
plt.ylabel(r'Intensity')
plt.legend()

arr = []

for i in phi:
    arr.append(1 / calculate_intensity(i, slit_width, slit_separation, wavelength, num_slits))


# wavelengths = np.linspace((1 / tmp_intensity1) * 1000, (1 / tmp_intensity2) * 1000, 1000)
colors = [wavelength_to_rgb(wl) for wl in arr]
color_map = np.array(colors).reshape(1, -1, 3)

plt.figure(figsize=(10, 2))
plt.imshow(color_map, extent=[-0.02, 0.02, 0, 1], aspect='auto')
plt.xlabel(r'$\varphi$, rad')
plt.yticks([])
plt.show()
