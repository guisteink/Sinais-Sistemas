'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np

def main():

    fig, ax = plt.subplots(3, 1, figsize=(6,6))

    #degrau u[n]
    n = np.arange(-10, 100, 1)
    l = np.size(n)
    u = np.zeros(l)
    ind = np.where(n >= 0)
    u[ind] = 1
    x = u

    #h[n]
    h = pow((3 / 4), n) * x

    ax[0].stem(n, u)
    ax[0].set_title('x[n] = u[n]')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('n')
    ax[0].set_xlim(-10, 10)
    ax[0].grid(True)

    ax[1].stem(n, h)
    ax[1].set_title('h[n] = pow((3/4),n).u[n]')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('n')
    ax[1].set_xlim(-10, 10)
    ax[1].grid(True)

    y = np.convolve(x, h)
    n2 = np.arange(-9.5, 100, 0.5)
    ax[2].stem(n2, y)
    ax[2].set_title('y[n] = h[n] * x[n]')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('n')
    ax[2].set_xlim(-10, 100)
    ax[2].grid(True)

    fig.tight_layout()
    plt.show()

main()