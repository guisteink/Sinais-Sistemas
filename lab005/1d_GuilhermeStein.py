'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift

#Exercicio 1 (d)
def main():
    fig, ax = plt.subplots(2, 2, figsize = (10,4))

    # retorna o sinal como soma de impulsos, foi a forma que consegui
    def sinal(k):
        v = []
        for i in range(len(k)):

            if k[i] == -9:
                v.insert(i, .25)
            elif k[i] == -8:
                v.insert(i, .5)
            elif k[i] == -7:
                v.insert(i, .75)
            elif k[i] == -6:
                v.insert(i, 1)

            elif k[i] == -4:
                v.insert(i, .25)
            elif k[i] == -3:
                v.insert(i, .5)
            elif k[i] == -2:
                v.insert(i, .75)
            elif k[i] == -1:
                v.insert(i, 1)

            elif k[i] == 1:
                v.insert(i, .25)
            elif k[i] == 2:
                v.insert(i, .5)
            elif k[i] == 3:
                v.insert(i, .75)
            elif k[i] == 4:
                v.insert(i, 1)

            elif k[i] == 6:
                v.insert(i, .25)
            elif k[i] == 7:
                v.insert(i, .5)
            elif k[i] == 8:
                v.insert(i, .75)
            elif k[i] == 9:
                v.insert(i, 1)

            else:
                v.insert(i, 0)
        return v

    N = 5
    nper = 2
    k = np.arange(-10, nper*N)
    x = sinal(k)
    ax[0][0].stem(k, x)
    ax[0][0].set_title('(c) x[n] original')
    ax[0][0].set_ylabel('amp')
    ax[0][0].set_xlabel('k')
    ax[0][0].grid(True)

    # DTFS
    X = fft(x) / len(x)

    # vetor frequencia
    w = fftfreq(len(k), d = 1 / N)

    # freq. zero no meio do grafico
    Xd = fftshift(X)
    w = fftshift(w)

    # modulo magnitude do espectro
    ModX = np.abs(Xd)

    # fase do espectro
    phasX = np.angle(Xd)

    # filtragem dos sinais muito pequenos
    phasX[ModX < 0.00001] = 0

    # retornando o sinal ao dominio do tempo
    xr = ifft(X) * len(x)

    # ignorando erros de arredondamento
    xr = np.real(xr)

    # plots das magnitudes e fases
    ax[1][0].stem(k, xr)
    ax[1][0].set_title('x[n]')
    ax[1][0].set_ylabel('amp')
    ax[1][0].set_xlabel('k')
    ax[1][0].grid(True)

    ax[0][1].stem(w, ModX)
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