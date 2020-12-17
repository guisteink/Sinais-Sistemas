'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift
from scipy import signal

#Exercicio 3
def main():
    fig, ax = plt.subplots(2, 1, figsize=(8,6))

    # definindo o sinal continuo periodico como no exemplo
    fs = 1.333
    wo = 2 * np.pi * fs
    Ts = 1/fs
    Tam = Ts/100

    # tempo e x(t)
    t = np.arange(0, Ts, Tam)
    x = signal.sawtooth(wo * t) * 0.88 + 0.12

    # fs
    X = fft(x)/len(x)

    # freq
    w = fftfreq(len(t), d=(1/Ts) * Tam)

    # freq zero no meio do grafico
    Xd = fftshift(X)
    w = fftshift(w)

    # magnitude e espectro
    modX = np.abs(Xd)

    # fase
    phasX = np.angle(Xd)

    # arrendondando
    phasX[modX < 0.00001] = 0

    # retornando ao dominio do tempo
    xr = ifft(X)*len(x)
    xr = np.real(xr)

    # magnitude
    ax[0].stem(w, modX)
    ax[0].set_title('Magnitude')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('tempo')
    ax[0].grid(True)

    # fase
    ax[1].stem(w, phasX)
    ax[1].set_title('Fase')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('tempo')
    ax[1].grid(True)

    fig.tight_layout()
    plt.show()

main()