from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def main():

    n1 = np.arange(0,100)
    n2 = np.arange(-4,96)

    x1 = signal.sawtooth((np.pi / 8)*n1, 0.5)
    x2 = signal.sawtooth((np.pi/8)*n2, 0.5)
    y = x1 + 0.9 * x2

    fig, ax = plt.subplots(3,1)

    #x1
    ax[0].set_title('x1[n1] = signal.sawtooth((pi/8)*n1)')
    ax[0].set_xlabel("n")
    ax[0].set_ylabel("Amplitude")
    ax[0].grid(True)
    ax[0].legend()
    ax[0].stem(n1,x1,'c-')


    #x2
    ax[1].set_title('x2 = signal.sawtooth((pi/8)*n2))')
    ax[1].set_xlabel("n")
    ax[1].set_ylabel("Amplitude")
    ax[1].grid(True)
    ax[1].legend()
    ax[1].stem(n2, x2, 'c-')

    #y
    ax[2].set_title('y = x1 + 0.9 * x2')
    ax[2].set_xlabel("n")
    ax[2].set_ylabel("Amplitude")
    ax[2].grid(True)
    ax[2].legend()
    ax[2].stem(n1, y, 'c-')

    fig.tight_layout()
    plt.show()

main()