'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift
from scipy import signal

#Exercicio 2
def square(wt, duty):
    sq = signal.square(wt, duty)
    return sq

def main():
    # figura
    fig, ax = plt.subplots(2, 1)

    # amostragem
    fs = 100
    w0 = 2*np.pi*fs
    Ts = 1/fs
    Tam = Ts/1000
    j = complex(0, 1)

    #sinal e plot
    Np = 3
    t = np.arange(0, Ts * Np, Tam)
    duty = 0.5
    s = 2.5*square(10*w0*t, duty)

    ax[0].plot(t, s)
    ax[0].set_title('s(t)')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('w')
    ax[0].grid(True)

    frand = np.random.rand(2)
    Vfrq = (1 + np.cos(200*t + (np.pi*frand[0]))) * (100/2)
    Vdc = (1 + np.cos(200*t + (np.pi*frand[1]))) * (5/2)
    ns = Vdc + 2.5*np.sin(2*np.pi*Vfrq*t)

    x = s + ns
    ax[1].plot(t, x)
    ax[1].set_title('ns(t)')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('w')
    ax[1].grid(True)

    fig.tight_layout()
    plt.show()

main()