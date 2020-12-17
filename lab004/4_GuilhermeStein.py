'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np

def main():

    fig, ax = plt.subplots(3, 1)
    fig2, ax2 = plt.subplots(3, 1)

    n = np.arange(-2, 21, 1)

    u = np.heaviside(n, 1)

    # a
    a = pow(1/2, 2)*u
    ax[0].stem(n, a)
    ax[0].set_title('(a) pow(1/2,2).u(t)')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('n')
    ax[0].set_xlim(-2, 20)
    ax[0].grid(True)

    # b
    def sinalB(n):
        v = []
        for i in range(len(n)):
            # como o array começa em -2, tive que acertar as posições pq ele entende que i = 0
            # é a posição -2 do array de tempo n. portanto sao as posiçoes 0 e 1 como foi plotado
            if(i == 2 or i == 3):
                v.append(1)
            else:
                v.append(0)
        return v

    b = sinalB(n)
    ax[1].stem(n, b)
    ax[1].set_title('(b) &[n] - &[n-1]')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('n')
    ax[1].set_xlim(-2, 20)
    ax[1].grid(True)

    #c
    def sinalC(n):
        v = []
        for i in range(len(n)):
            if (i % 2) == 0:
                v.append(1)
            else:
                v.append(-1)
        return v

    nC = np.arange(-2, 4, 1)
    c = sinalC(nC)
    ax[2].stem(nC, c)
    ax[2].set_title('(c) pow(-1,n).(u[n+2] - u[n-3])')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('n')
    ax[2].set_xlim(-2, 20)
    ax[2].grid(True)

    # d
    n = np.arange(-2, 21, 1)
    u = np.heaviside(n, 1)
    ax2[0].stem(n, u)
    ax2[0].set_title('(d) u[n]')
    ax2[0].set_ylabel('amp')
    ax2[0].set_xlabel('n')
    ax2[0].set_xlim(-2, 20)
    ax2[0].grid(True)

    # e
    e = (-n) * u
    ax2[1].stem(n, e)
    ax2[1].set_title('(e) (-n).u[n]')
    ax2[1].set_ylabel('amp')
    ax2[1].set_xlabel('n')
    ax2[1].set_xlim(-2, 20)
    ax2[1].grid(True)

    # f
    nF = np.arange(0, 4, 1)
    u = np.heaviside(nF, 1)
    f = np.sin((1/12) * nF * np.pi) * u
    ax2[2].stem(nF, f)
    ax2[2].set_title('(f) (sen(n*pi/12).u[n-3]')
    ax2[2].set_ylabel('amp')
    ax2[2].set_xlabel('n')
    ax2[2].set_xlim(-2, 20)
    ax2[2].grid(True)


    fig.tight_layout()
    plt.show()
main()