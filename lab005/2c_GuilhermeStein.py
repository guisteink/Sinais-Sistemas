'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import ifft, fftfreq

def modulo_sinal(k):
    v = []
    for i in range(len(k)):
        if k[i] == 3:
            v.insert(i, 1)
        elif k[i] == 4:
            v.insert(i, 1)
        elif k[i] == 9:
            v.insert(i, 1)
        elif k[i] == 10:
            v.insert(i, 1)
        else:
            v.insert(i, 0)
    return v

def fase_sinal(k):
    v = []
    for i in range(len(k)):
        if k[i] == 3:
            v.insert(i, -1)
        elif k[i] == 4:
            v.insert(i, 1)
        elif k[i] == 10:
            v.insert(i, -1)
        elif k[i] == 11:
            v.insert(i, 1)
        else:
            v.insert(i, 0)
    return v

def polar_to_rect(A, phi):
    return complex(A * np.cos(phi), A * np.sin(phi) * np.pi/2)

#Exercicio 2 c
def main():
    fig, ax = plt.subplots(3, 1, figsize = (6,6))

    # amostragem
    N = 7
    nper = 1
    k = np.arange(0, nper*N)

    # modulo e fase
    modX = modulo_sinal(k)
    phasX = fase_sinal(k)

    # vetor da frequencia
    w = fftfreq(len(k), d=1/N)

    # inserindo os valores no Xk
    Xk = []
    for i in range(len(k)):
        Xk.insert(i, polar_to_rect(modX[i], phasX[i] * np.pi/2))

    xr = ifft(Xk) * len(k)
    xr = np.real(xr)

    # plot
    ax[0].stem(k, modX)
    ax[0].set_title('|X[k]|')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('k')
    ax[0].grid(True)

    ax[1].stem(k, phasX)
    ax[1].set_title('angle(X[k])')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('k')
    ax[1].grid(True)

    ax[2].stem(w, xr)
    ax[2].set_title('x[n]')
    ax[2].set_ylabel('amp')
    ax[2].set_xlabel('k')
    ax[2].grid(True)

    fig.tight_layout()
    plt.show()

main()