from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def main():

    n = np.linspace(0,5,20)
    #sinal degrau
    x = np.heaviside(n, 1)
    n1 = np.linspace(-1,5,20)
    n2 = np.linspace(1,5,20)
    fig, ax = plt.subplots(3,1)

    #a
    ax[0].stem(n2, x, 'c-')
    ax[0].set_title('(a) u[n-1] -> sinal degrau em tempo discreto deslocado para frente')
    ax[0].set_ylabel('Amplitude')
    ax[0].set_xlabel('n')
    ax[0].set_xlim(-5, 5)
    ax[0].grid(True)

    #b
    ax[1].stem(n, x, 'c-')
    ax[1].set_title('(b) u[n] -> sinal degrau em tempo discreto')
    ax[1].set_ylabel('Amplitude')
    ax[1].set_xlabel('n')
    ax[1].set_xlim(-5,5)
    ax[1].grid(True)

    # c
    ax[2].stem(n1, x, 'c-')
    ax[2].set_title('(c) u[n+1] -> sinal degrau em tempo discreto deslocado para tras')
    ax[2].set_ylabel('Amplitude')
    ax[2].set_xlabel('n')
    ax[2].set_xlim(-5, 5)
    ax[2].grid(True)

    fig.tight_layout()
    plt.show()




main()