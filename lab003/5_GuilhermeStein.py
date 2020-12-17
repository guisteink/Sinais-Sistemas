'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots(3, 1, figsize=(6, 6))

    n1 = np.linspace(0, 4, 4)
    n2 = np.linspace(0, 6, 6)

    #x
    x = np.heaviside(n1, 1)
    ax[0].stem(n1, x)
    ax[0].set_title('x[n]')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('n')
    ax[0].set_xlim(0, 20)
    ax[0].grid(True)

    #h
    α = 7/9
    h = pow(α, n2) * np.heaviside(n2, 1)
    ax[1].stem(n2, h)
    ax[1].set_title('h[n]')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('n')
    ax[1].set_xlim(0, 20)
    ax[1].grid(True)

    #y
    y = np.convolve(h, x)
    ny = np.linspace(0, 9, 9)
    ax[2].stem(ny, y)
    ax[2].set_title('y[n]')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('n')
    ax[2].set_xlim(0, 20)
    ax[2].grid(True)

    fig.tight_layout()
    plt.show()
main()