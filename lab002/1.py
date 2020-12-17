import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

def main():

    t = np.arange(0, np.pi/30, 0.001)
    x1 = 2*np.cos(30*np.pi*t)

    fig2, ax = plt.subplots()
    ax.plot(t,x1,'c-',linewidth = 1, label = "x1(t) = 2*cos(30*pi*t)")
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    plt.scatter(0.016667*4,2,color='red')
    plt.scatter(0.016667*2,-2,color='red')
    ax.legend()
    fig2.show()

    plt.show()

main()