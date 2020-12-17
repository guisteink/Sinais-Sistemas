from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def main():
    t = np.linspace(0, 1, 1000)
    x = signal.square(10 * np.pi * t, 0.2)

    plt.plot(t, x)
    plt.title('Onda quadrada x(t) = square(10*pi*t)')
    plt.xlabel('Tempo t, em segundos')
    plt.ylabel('Amplitude')

    # limite de y
    plt.ylim(-2, 2)

    # sistema de grid (quadriculado)
    plt.grid(True)

    plt.show()

main()
