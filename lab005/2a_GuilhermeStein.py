'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import ifft, fftfreq

#Exercicio 2 (a)
def main():
    fig, ax = plt.subplots(2, 1)

    # amostragem
    N = 17
    nper = 1
    n = np.arange(0, nper*N)

    # sinal
    x = np.cos((np.pi * 6 * n)/17)

    # vetor de frequencia
    w = fftfreq(len(n), d=1/N)

    # recuperação do sinal no dominio
    xr = ifft(x) * len(n)
    xr = np.real(xr)

    # plot
    ax[0].stem(w, xr)
    ax[0].set_title('(a)')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('amostras')
    ax[0].grid(True)

    ax[1].text(0.5,0.5, 'X[k] = cos(6*pi*n)/17, período N = 17.', horizontalalignment='center', verticalalignment='center')
    ax[1].text(0.5, 0.6, 'X[k] -> DTFS -> x[n] = { 0, n != +-3 e 17/2, n = +-3 }',horizontalalignment='center', verticalalignment='center')

    fig.tight_layout()
    plt.show()

main()