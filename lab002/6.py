from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def main():

    t = np.arange(0, 2.5, 0.001)
    x1 = 10 * pow(np.e, -2*t) * np.sin(30 * np.pi * t + np.pi/2)
    x2 = 10 * pow(np.e, -2 * t) * np.sin(30 * np.pi * t)
    x3 = 10 * pow(np.e, 2 * t) * np.sin(30 * np.pi * t)

    fig, ax = plt.subplots(3, 1)

    #a
    ax[0].plot(t, x1, 'c-', linewidth=1, label="")
    ax[0].set_title('x = 10 * pow(np.e, -2*t) * np.sin(30 * np.pi * t + np.pi/2)')
    ax[0].set_ylabel('Amplitude')
    ax[0].set_xlabel('Tempo t, em segundos')
    ax[0].grid(True)

    #b
    ax[1].plot(t, x2, 'c-', linewidth=1)
    ax[1].set_title('x = 10 * pow(np.e, -2 * t) * np.sin(30 * np.pi * t)')
    ax[1].set_ylabel('Amplitude')
    ax[1].set_xlabel('Tempo t, em segundos')
    ax[1].grid(True)

    #c
    ax[2].plot(t, x3, 'c-', linewidth=1)
    ax[2].set_title('x = 10 * pow(np.e, 2 * t) * np.sin(30 * np.pi * t)')
    ax[2].set_ylabel('Amplitude')
    ax[2].set_xlabel('Tempo t, em segundos')
    ax[2].grid(True)

    fig.tight_layout()
    plt.show()









main()