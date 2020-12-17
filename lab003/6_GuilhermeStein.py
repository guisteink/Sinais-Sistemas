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

    #x(t)
    t = np.linspace(0, 1, 10)
    x = np.heaviside(t, 1)
    ax[0].plot(t, x)
    ax[0].set_title('x(t) = u(t) - u(t-1)')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('t')
    ax[0].set_xlim(-5, 5)
    ax[0].grid(True)

    #h(t)
    t2 = np.linspace(0, 100, 1000)
    u = np.heaviside(t2, 1)
    h = pow(np.e, -t2) * u
    ax[1].plot(t2, h)
    ax[1].set_title('h(t) = pow(e,-t) * u(t)')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('t')
    ax[1].set_xlim(-10, 10)
    ax[1].grid(True)

    #y(t)
    y = np.convolve(h, x) * Ts
    ty = np.linspace(0, 1009, 1009)
    ax[2].plot(ty, y)
    ax[2].set_title('y(t) = x(t) * h(t)')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('t')
    ax[2].set_xlim(-50, 50)
    ax[2].grid(True)

    fig.tight_layout()
    plt.show()
main()