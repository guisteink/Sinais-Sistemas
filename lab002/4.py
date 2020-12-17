from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def main():
    t = np.linspace(0, 1, 1000)
    x = signal.sawtooth(10 * np.pi * t, 0.5)

    plt.plot(t, x)
    plt.title('Onda triangular x(t) = sawtooth(10*pi*t)')
    plt.xlabel('Tempo t, em segundos')
    plt.ylabel('Amplitude')

    # limite de y
    plt.ylim(-2, 2)
    plt.xlim(0, 1)

    # sistema de grid (quadriculado)
    plt.grid(True)

    plt.show()

main()
