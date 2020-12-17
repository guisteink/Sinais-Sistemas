'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift

#Exercicio 1 (b)
def main():
    fig, ax = plt.subplots(3, 1)

    # vetor de amostragem
    N = 21
    nper = 10
    n = np.arange(0, nper * N)

    # vetor do sinal
    xp1 = np.ones(len(n))
    x = np.sin((4*np.pi*n)/21) + np.cos((10*np.pi*n)/21) + xp1

    # calculando a dtfs
    X = fft(x)/len(x)

    # vetor da freq
    w = fftfreq(len(n), d = 1/N)

    # posicionando a freq. zero no meio do grafico
    Xd = fftshift(X)
    w = fftshift(w)

    # calculo do modulo da magnitude no espectro
    ModX = np.abs(Xd)

    # calculo da fase do espectro
    phasX = np.angle(Xd)

    # filtragem dos sinais mto pequenos
    phasX[ModX < 0.00001] = 0

    # tornando o sinal para o dominio do tempo novamente
    xr = ifft(X)*len(x)

    # ignroando erros de arrendomento das transformadas
    xr = np.real(xr)

    #plots
    ax[0].stem(n, xr)
    ax[0].set_title('(b) x[n]')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('amostras')
    ax[0].grid(True)

    ax[1].stem(w, ModX)
    ax[1].set_title('|X[k]|')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('k')
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