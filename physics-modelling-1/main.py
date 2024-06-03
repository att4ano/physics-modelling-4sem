import numpy as np
import matplotlib.pyplot as plt


def intensity(x, wavelength, L, d, b, N):
    theta = np.arctan(x / L)
    beta = (np.pi * d * np.sin(theta)) / wavelength
    I = (np.sin(N * beta) / np.sin(beta)) ** 2 * (np.sin(beta / d * b) / (beta / d * b)) ** 2
    return I


def normalize(I):
    return I / np.max(I)


def calculate_total_intensity(x, wavelengths, L, d, b, N):
    I_total = np.zeros_like(x)
    for wavelength in wavelengths:
        I_total += intensity(x, wavelength, L, d, b, N)
    return I_total


def plot_intensity(x, I_mono, I_total, lambda_0, delta_lambda):
    plt.figure(figsize=(12, 6))
    plt.plot(x, I_mono, label=f'Монохроматический свет ($\\lambda_0 = {lambda_0 * 1e9:.0f}$ нм)')
    plt.plot(x, I_total, linestyle='--',
             label=f'Квазимонохроматический свет ($\\lambda_0 = {lambda_0 * 1e9:.0f}$ нм, $\\Delta \\lambda = {delta_lambda * 1e9:.0f}$ нм)')
    plt.xlabel('Координата x (м)')
    plt.ylabel('Интенсивность')
    plt.title('Дифракционная картина монохроматического и квазимонохроматического света')
    plt.legend()
    plt.grid(True)
    plt.show()


lambda_0 = 500e-9  # центральная длина волны в метрах
delta_lambda = 300e-9  # спектральная ширина в метрах

period = 1e-6  # период решетки в метрах
height = 1e-6  # высота щели в метрах
num_gaps = 1000  # число щелей

L = 1.0  # расстояние до экрана в метрах

x = np.linspace(-0.1, 0.1, 1000000)  # диапазон координат x в метрах

I_mono = intensity(x, lambda_0, L, period, height, num_gaps)
wavelengths = np.linspace(lambda_0 - delta_lambda / 2, lambda_0 + delta_lambda / 2, 100)
I_total = calculate_total_intensity(x, wavelengths, L, period, height, num_gaps)

I_mono = normalize(I_mono)
I_total = normalize(I_total)

plot_intensity(x, I_mono, I_total, lambda_0, delta_lambda)
