'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots(4, 1)

    def sinal_trem_impulso(t, T):
        ti = []
        for i in range(len(t)):
            if(i % T == 0):
                ti.append(1)
            else:
                ti.append(0)
        return ti

    def sinal_triang(t):
        tri = []
        for i in range(len(t)):
            if t[i] == -1:
                tri.append(0)
            if t[i] == 0:
                tri.append(1)
            if t[i] == 1:
                tri.append(0)
        return tri


    t = np.arange(-4, 21, 1)
    x = sinal_triang(t)

    # a
    Ta = 4
    trem_a = sinal_trem_impulso(t, Ta)
    y = np.convolve(x, trem_a)
    t = np.arange(-4, 23, 1)
    ax[0].plot(t, y)
    ax[0].set_title('(a) T = 4')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('t')
    ax[0].set_xlim(-4, 21, 1)
    ax[0].grid(True)

    # b
    Tb = 2
    t = np.arange(-2, 23, 1)
    trem_b = sinal_trem_impulso(t, Tb)
    t = np.arange(-2, 25, 1)
    y = np.convolve(x, trem_b)
    ax[1].plot(t, y)
    ax[1].set_title('(b) T = 2')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('t')
    ax[1].set_xlim(-2, 21, 1)
    ax[1].grid(True)

    # c
    Tc = 3 / 2
    t = np.arange(-6, 23, 1)
    trem_c = sinal_trem_impulso(t, Tc)
    t = np.arange(-6, 25, 1)
    y = np.convolve(x, trem_c)
    ax[2].plot(t, y)
    ax[2].set_title('(c) T = 3/2')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('t')
    ax[2].set_xlim(-6, 21, 1)
    ax[2].grid(True)

    # d
    Td = 1
    t = np.arange(-2, 23, 1)
    trem_d = sinal_trem_impulso(t, Td)
    t = np.arange(-2, 25, 1)
    y = np.convolve(x, trem_d)
    ax[3].plot(t, y)
    ax[3].set_title('(d) T = 1')
    ax[3].set_ylabel('amp')
    ax[3].set_xlabel('t')
    ax[3].set_xlim(-2, 25, 1)
    ax[3].grid(True)


    fig.tight_layout()
    plt.show()
main()