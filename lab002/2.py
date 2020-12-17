import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

def main():

    t = np.arange(0, np.pi/30, 0.001)

    #x1(t)
    x1 = 2*np.cos(30*np.pi*t)

    #x2(t)
    x2 = x1 + 2.5*np.cos(60*np.pi*t)

    fig, ax = plt.subplots()
    ax.plot(t, x2, 'c-', linewidth=1, label="x2(t) = x1(t) + 2.5cos(60*pi*t)")
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    ax.legend()
    fig.show()

    plt.show()

main()