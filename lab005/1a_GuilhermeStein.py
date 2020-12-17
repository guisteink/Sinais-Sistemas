'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift

#Exercicio 1 (a)
def main():
    fig, ax = plt.subplots(3, 1)

    #criando o vetor de amostra N
    N_PERIODO = 13
    nper = 10
    n = np.arange(0, nper*N_PERIODO)

    #vetor do sinal
    x = np.cos((6*np.pi)*n/13 + np.pi/6)

    #DTFS
    X = fft(x)/len(x)

    #vetor frequencia
    w = fftfreq(len(n), d = 1/N_PERIODO)

    #freq. zero no meio do grafico
    Xd = fftshift(X)
    w = fftshift(w)

    #modulo magnitude do espectro
    ModX = np.abs(Xd)

    #fase do espectro
    phasX = np.angle(Xd)

    #filtragem dos sinais muito pequenos
    phasX[ModX < 0.00001] = 0

    #retornando o sinal ao dominio do tempo
    xr = ifft(X)*len(x)

    #ignorando erros de arredondamento
    xr = np.real(xr)

    #plot
    ax[0].stem(n, xr)
    ax[0].set_title('(a) x[n]')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('amostras')
    ax[0].set_xlim(0, 20)
    ax[0].grid(True)

    ax[1].stem(w, ModX)
    ax[1].set_title('|X[k]|')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('k')
    ax[1].set_xlim(-10, 10)
    ax[1].grid(True)

    ax[2].stem(w, phasX)
    ax[2].set_title('angle(|X[k]|)')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('k')
    ax[2].set_xlim(-5, 5)
    ax[2].grid(True)

    fig.tight_layout()
    plt.show()

main()