'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import ifft, fftfreq

#Exercicio 2 d
def main():
    fig, ax = plt.subplots(2, 1)

    # amostragem
    N = 7
    nper = 2
    n = np.arange(-3, nper*N)

    # sinal xk
    def sinalXk(n):
        v = []
        for i in range(len(n)):
            if n[i] == -15:
                v.insert(i, -0.5)
            elif n[i] == -14:
                v.insert(i, 1)
            elif n[i] == -8:
                v.insert(i, 1)
            elif n[i] == -7:
                v.insert(i, -0.5)
            elif n[i] == -6:
                v.insert(i, 1)
            elif n[i] == -1:
                v.insert(i, 1)
            elif n[i] == 0:
                v.insert(i, -0.5)
            elif n[i] == 1:
                v.insert(i, 1)
            elif n[i] == 6:
                v.insert(i, 1)
            elif n[i] == 7:
                v.insert(i, -0.5)
            elif n[i] == 8:
                v.insert(i, 1)
            elif n[i] == 13:
                v.insert(i, 1)
            else:
                v.insert(i, 0)
        return v

    x = sinalXk(n)

    # vetor da frequencia
    w = fftfreq(len(n), d=1 / N)

    # recuperação do sinal no dominio
    xr = ifft(x) * len(n)
    xr = np.real(xr)

    # plot
    ax[0].stem(n, x)
    ax[0].set_title('(d) Sinal original X[k]')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('amostras')
    ax[0].grid(True)

    ax[1].stem(w, xr)
    ax[1].set_title('x[n]')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('amostras')
    ax[1].grid(True)


    fig.tight_layout()
    plt.show()

main()