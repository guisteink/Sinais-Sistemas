'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi
from scipy.fft import fft, ifft, fftfreq, fftshift

def AnalisadorEspectro(x,t,N,Lfreq,titleTempo,titleFreq, nameFigure):
    # sinal x, vetor de tempo t
    # N - tamanho da fft
    # Lfreq - limite superior da frequencia
    # titletempo e titlefreq - title dos graficos do tempo e da freq.


    # calculando sua FT
    Tam = t[1]-t[0]
    X = fft(x, N)*Tam
    w = fftfreq(len(X), d=Tam)
    # Os indices de frequencia são mudados de 0 a N-1 para -N/2 + 1 a N/2
    # posicionando a freq. zero no meio do gráfico
    wd = fftshift(w)
    Xd = fftshift(X)

    # calculando o modulo - magnitude do espectro
    ModX = np.abs(Xd)

    fig, ax = plt.subplots(2, 1)
    fig.canvas.set_window_title(nameFigure)
    ax[0].plot(t, x, lw=2, label="x(t)")
    ax[0].set_ylabel("Amplitude")
    ax[0].set_xlabel("tempo [s]")
    ax[0].grid(True)
    ax[0].set_title(titleTempo)

    ax[1].plot(wd, ModX, 'r-', lw=2, label="|X(jw)|")
    ax[1].set_ylabel("Amplitude")
    ax[1].set_xlabel("Freq. [Hz]")
    ax[1].grid(True)
    if Lfreq != 0:
        ax[1].set_xlim(0, Lfreq)
    ax[1].set_title(titleFreq)
    fig.tight_layout()

    return ModX,wd

def Filtragem_RC(x, t, T,Tam, RC=[0.1, 0.35, 1.2]):
    # sinal x, vetor de tempo t
    # T - periodo de x
    # Tam - taxa de amostragem
    # RC - valores para RC do filtro
    ## filtragem

    X = fft(x) / len(x)
    # criando o vetor de frequencia
    w = fftfreq(len(t), d=(1 / T) * Tam)

    for RCk in RC:
        H = 1 / (1 + ((1j * w) * (RCk))) # passa-baixas
        Y = H * X  # aplicando o filtro
        # retornando o sinal ao dominio do tempo
        yt = ifft(Y) * len(x)
        yr = np.real(yt)  # ignorando os erros de arrendondamento do fft e ifft

    # plotando as figuras para visualização
    fig1, ax1 = plt.subplots(1, 1)
    fig1.canvas.set_window_title("Filtragem")
    ax1.plot(t, x, linewidth=2, label="xr(t)")
    ax1.plot(t, yr, 'r--', linewidth=1, label="xr_filtrado(t)")
    ax1.set_ylabel("Amplitude")
    ax1.set_xlabel("tempo [s]")
    ax1.grid(True)
    ax1.legend()
    ax1.set_title('xr(t) e xr_filtrado(t) para RC = ' + str(RCk))

    return yr

# definindo o sinal no tempo continuo
f  = 100        # freq. do sinal contínuo
w0 = 2*pi*f    # frequencia angular
T = 1/f       # período fundamental do sinal


# criando o sinal para ser amostrado para o T =0.001
Tamc = T/1000   # período de amostragem para representar o sinal continuo 1000 vezes menor que o período do sinal

# Criando o vetor de tempo,3 períodos, e intervalo de Tam
t = np.arange(0, T*6, Tamc)
x = 100*np.cos(w0*t)
Modx, wd = AnalisadorEspectro(x, t, 2 ** 23, 2500, 'x(t)' , '|X(jw)|', 'Ts = ' + str(T))

# Fazendo a amostragem
Ts = T/10     # periodo do trem de impulso

t2 = np.arange(0, (T*6)+1, Ts)
x2 = 100*np.cos(w0*t2)

# Retentor de ordem 1
xr = np.interp(t, t2, x2)
AnalisadorEspectro(xr, t, 2**22, 2500, 'xs(t)', '|Xs(jw)|', 'Ts = ' + str(Ts))

#reconstru~çao do sinal cm o retentor

# filtragem
RC = [0.35]
xrf = Filtragem_RC(xr, t, T, Tamc,RC)
AnalisadorEspectro(xrf, t, 2 ** 20, 2500, 'xs(t)' +' filtrado com RC ='+str(RC[0]), '|Xs(jw)|', 'Ts = ' + str(Ts))

# sinal para ser amostrado para o periodo de amostragem de 0.0025
Tamc = T/2004
Ts = T/4     # periodo do trem de impulso

# Retentor de ordem um (interpolação)
t3 = np.arange(0,(T*6)+1,Ts)
x3 = 100*np.cos(w0*t3)

xr2 = np.interp(t, t3, x3)
AnalisadorEspectro(xr2, t, 2 ** 21, 2500, 'xs(t)' , '|Xs(jw)|', 'Ts = ' + str(Ts))

# filtragem
xrf2 = Filtragem_RC(xr2, t, T, Tamc, RC = [0.35])
AnalisadorEspectro(xrf2, t, 2 ** 20, 2500, 'xs(t)', '|Xs(jw)|', 'Ts = ' + str(Ts))


plt.show()