'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots(3, 1, figsize=(6, 6))
    Ts = 0.0001

    #x
    t = np.linspace(0, 1, 2)
    x = np.heaviside(t, 1)
    ax[0].plot(t, x)
    ax[0].set_title('x(t)')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('t')
    ax[0].set_xlim(-3, 3)
    ax[0].grid(True)

    #t
    t2 = np.linspace(0, 2, 2)
    h = np.heaviside(t2, t2)
    ax[1].plot(t2, h)
    ax[1].set_title('h(t)')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('t')
    ax[1].set_xlim(-3, 3)
    ax[1].grid(True)

    #y
    ty = np.linspace(0, 3, 3)
    y = np.convolve(h, x) * Ts
    ax[2].plot(ty, y)
    ax[2].set_title('y(t)')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('t')
    ax[2].set_xlim(-5, 5)
    ax[2].grid(True)


    fig.tight_layout()
    plt.show()
main()