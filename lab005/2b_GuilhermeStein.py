'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import ifft, fftfreq

#Exercicio 2 (b)
def main():
    fig, ax = plt.subplots(2, 1)

    # amostragem
    N = 21
    nper = 1
    n = np.arange(0, nper*N)

    # sinal
    j = complex(0, 1)
    x = np.cos(10*np.pi*n/21) + j*np.cos(4*np.pi*n/21)

    # vetor da frequencia
    w = fftfreq(len(n), d=1/N)

    # recuperação do sinal no dominio
    xr = ifft(x * len(n))
    xr = np.real(xr)

    # plot
    ax[0].stem(w, xr)
    ax[0].set_title('(b)')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('amostras')
    ax[0].grid(True)

    ax[1].text(0.5, 0.5, 'X[k] = cos(10*pi*n)/21 + j*sen(4*pi*n/21), período N = 21.',
               horizontalalignment='center', verticalalignment='center')
    ax[1].text(0.5, 0.7, 'X[k] -> DTFS -> x[n] = { 21/2, n = +-5 e 0, n != +-3 }', horizontalalignment='center',
               verticalalignment='center')

    fig.tight_layout()
    plt.show()

main()