'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots(3, 1, figsize=(6, 6))

    n = np.linspace(0, 20, 40)
    u = np.heaviside(n, 1)

    #x
    α = 4/5
    x = pow(α, n) * u
    ax[0].stem(n, x)
    ax[0].set_title('x[n] = pow(α,n).u[n], onde α = 4/5.')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('n')
    ax[0].set_xlim(0, 20)
    ax[0].grid(True)

    #h
    h = u
    ax[1].stem(n, h)
    ax[1].stem(n, h)
    ax[1].set_title('h[n] = u[n]')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('n')
    ax[1].set_xlim(0, 20)
    ax[1].grid(True)

    #y - convolucao
    y = np.convolve(h, x)
    ny = np.linspace(0, 79, 79)
    ax[2].stem(ny, y)
    ax[2].set_title('y[n] = x[n] * h[n]')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('n')
    ax[2].set_xlim(-0, 20)
    ax[2].grid(True)


    fig.tight_layout()
    plt.show()
main()