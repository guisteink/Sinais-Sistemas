'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np

def main():

    fig, ax = plt.subplots(4, 1)

    t = np.arange(0, 0.2, 0.001)
    t0 = np.arange(0.05, 0.2, 0.001)

    # degrau u(t)
    u = np.heaviside(t, 1)
    ax[0].plot(t, u)
    ax[0].set_title('u(t)')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('t')
    ax[0].set_xlim(-0.05, 0.20)
    ax[0].grid(True)

    # (a) , quando t=0. v0(t) = R * 1, pois o ampop inversor ainda não esta ativo.
    ax[1].plot(t, (1 + 0.5*np.cos(20*np.pi*t)))
    ax[1].set_title('(a)v0(t)=R(t), t=0s. (amp-op inversor desativado)')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('t')
    ax[1].set_xlim(-0.05, 0.25)
    ax[1].grid(True)

    # (b), quando t = t0. vo(t) = -R(t) * v1(t) onde v1(t) = 1
    R = (1 + 0.5*np.cos(20*np.pi*t0))
    v0 = np.heaviside(t0, 1) * (-R)
    ax[2].plot(t0, v0)
    ax[2].set_title('(b)v0(t)=-R(t), t0=50milisegundos. (amp-op inversor ativado em t0)')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('t')
    ax[2].set_xlim(-0.05, 0.25)
    ax[2].grid(True)

    ax[3].text(0.5,0.5,'O sistema é variante no tempo.', horizontalalignment='center', verticalalignment='center')

    fig.tight_layout()
    plt.show()

main()