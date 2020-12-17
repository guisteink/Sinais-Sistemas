'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np

def main():

    fig, ax = plt.subplots(3, 1)

    n = np.arange(0, 8, .001)

    # x[n]
    x = np.heaviside(n, .001)
    ax[0].stem(n, x)
    ax[0].set_title('x[n] = u[n] - u[n-8]')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('n')
    ax[0].set_xlim(-1, 30)
    ax[0].grid(True)

    # h[n]
    h = np.sin(((2*np.pi)/8) * n) * x
    ax[1].stem(n, h)
    ax[1].set_title('h[n]')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('n')
    ax[1].set_xlim(-1, 30)
    ax[1].grid(True)

    y = np.convolve(x, h)
    nY = np.arange(0, 15.999, .001)
    ax[2].stem(nY, y)
    ax[2].set_title('y[n]')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('n')
    ax[2].set_xlim(0, 30)
    ax[2].grid(True)

    fig.tight_layout()
    plt.show()

main()