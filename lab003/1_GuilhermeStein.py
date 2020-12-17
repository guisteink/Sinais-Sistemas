'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots(4, 1)

    #plot de h
    n = np.linspace(0, 2, 3)
    h = np.heaviside(n, 1)
    ax[0].stem(n, h)
    ax[0].set_title('h[n]')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('n')
    ax[0].set_xlim(-3, 3)
    ax[0].grid(True)

    #plot de x, que coloquei como a soma do sinal a + b, dois impulsos
    #a
    n1 = np.arange(0, 2)
    l1 = np.size(n1)
    a_impulso = np.zeros(l1)
    ind = np.where(n == 0)
    a_impulso[ind] = 1
    # ax[1].stem(n1, a_impulso)
    # ax[1].set_title('sinal a')
    #ax[1].set_xlabel('n')
    #ax[1].set_xlim(-3, 3)
    #ax[1].set_ylabel('amp')
    #ax[1].grid(True)

    #b
    n2 = np.arange(0, 2)
    l2 = np.size(n2)
    b_impulso = np.zeros(l2)
    b_impulso = np.zeros(l2)
    ind = np.where(n == 1)
    b_impulso[ind] = 2
    #ax[2].stem(n2, b_impulso)
    #ax[2].set_title('sinal b')
    #ax[2].set_xlabel('n')
    #ax[2].set_xlim(-3, 3)
    #ax[2].set_ylabel('amp')
    #ax[2].grid(True)

    #x
    x = a_impulso + b_impulso
    ax[1].stem(n2, x)
    ax[1].set_title('x[n] = { 0.5 , n = 0 ; 2, n = 1 }')
    ax[1].set_xlabel('n')
    ax[1].set_xlim(-3, 3)
    ax[1].set_ylabel('amp')
    ax[1].grid(True)

    #y
    y = np.roll(x, n1)
    ax[2].stem(n1, y)
    ax[2].set_title('y[n] = h[n] * x[n] - roll')
    ax[2].set_xlabel('n')
    ax[2].set_xlim(-3, 3)
    ax[2].set_ylabel('amp')
    ax[2].grid(True)


    #y2 convolve
    y2 = np.convolve(h, x)
    ny = np.linspace(0, 4, 4)
    ax[3].stem(ny, y2)
    ax[3].set_title('y[n] = h[n] * x[n] - convolve')
    ax[3].set_xlabel('n')
    ax[3].set_xlim(-10, 10)
    ax[3].set_ylabel('amp')
    ax[3].grid(True)


    fig.tight_layout()
    plt.show()

main()