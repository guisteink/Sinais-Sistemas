'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift

#Exercicio 1 (c)
def main():
    fig, ax = plt.subplots(2, 2, figsize=(10,4))

    # retorna o sinal como soma de impulsos, foi a forma que consegui
    def sinal(k):
        v = []
        for i in range(len(k)):
            if k[i] == -10:
                v.insert(i, -1)
            elif k[i] == -6:
                v.insert(i, 1)
            elif k[i] == -2:
                v.insert(i, -1)
            elif k[i] == 2:
                v.insert(i, 1)
            elif k[i] == 6:
                v.insert(i, -1)
            elif k[i] == 10:
                v.insert(i, 1)
            else:
                v.insert(i, 0)
        return v

    N = 8
    nper = 1
    k = np.arange(0, nper*N)
    x = sinal(k)

    k2 = np.arange(-10, 11, 1)
    x2 = sinal(k2)

    ax[0][0].stem(k2, x2)
    ax[0][0].set_title('x[n] original')
    ax[0][0].set_ylabel('amp')
    ax[0][0].set_xlabel('k')
    ax[0][0].grid(True)

    # DTFS
    xF = fft(x) / len(x)

    # vetor frequencia
    w = fftfreq(len(k), d=1/N)

    # freq. zero no meio do grafico
    Xd = fftshift(xF)
    w = fftshift(w)

    # modulo magnitude do espectro e fase
    modX = np.abs(Xd)
    phasX = np.angle(Xd)
    # filtragem dos sinais muito pequenos
    phasX[modX < 0.00001] = 0

    # retornando o sinal ao dominio do tempo
    xr = ifft(xF) * len(x)

    # ignorando erros de arredondamento
    xr = np.real(xr)

    # plots das magnitudes e fases
    ax[1][0].stem(k, xr)
    ax[1][0].set_title('x[n]')
    ax[1][0].set_ylabel('amp')
    ax[1][0].set_xlabel('k')
    ax[1][0].grid(True)

    ax[0][1].stem(w, modX)
    ax[0][1].set_title('|X[k]|')
    ax[0][1].set_ylabel('amp')
    ax[0][1].set_xlabel('k')
    ax[0][1].grid(True)

    ax[1][1].stem(w, phasX)
    ax[1][1].set_title('angle(|X[k]|)')
    ax[1][1].set_ylabel('amp')
    ax[1][1].set_xlabel('k')
    ax[1][1].grid(True)

    fig.tight_layout()
    plt.show()

main()