'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots(3, 1, figsize=(6, 6))

    # h
    n1 = np.linspace(0, 10, 10)
    h = np.heaviside(n1, 1)
    ax[0].stem(n1, h)
    ax[0].set_title('h[n] = u[n] - u[n-10]')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('n')
    ax[0].set_xlim(0, 10)
    ax[0].grid(True)

    # x
    n2 = np.linspace(2, 7, 7)
    x = np.heaviside(n2, 1)
    ax[1].stem(n2, x)
    ax[1].set_title('x[n] = u[n-2] - u[n-7]')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('n')
    ax[1].set_xlim(0, 10)
    ax[1].grid(True)

    #y - convoluçao
    y = np.convolve(h, x)
    ny = np.linspace(0, 16, 16)
    ax[2].stem(ny, y)
    ax[2].set_title('y[n] = x[n] * h[n]')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('n')
    ax[2].set_xlim(0, 100)
    ax[2].grid(True)

    fig.tight_layout()
    plt.show()
main()