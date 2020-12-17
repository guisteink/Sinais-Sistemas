'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift
from scipy import signal

#Exercicio 1
def square(wt, duty):
    sq = signal.square(wt, duty)
    return sq

def main():
    # figura 1 plot FS
    fig, ax = plt.subplots(2, 1, figsize=(8, 8))

    # tempo de amostragem
    t = np.arange(0, 4, 0.01)
    w0 = 2*np.pi
    j = complex(0, 1)

    #sinal
    duty = 0.25
    xs = 0.5+0.5*square(w0*t, duty)

    # fs
    X = fft(xs) / len(xs)

    # dominio da frequencia
    W = fftfreq(len(t), d=1/80)

    # fase e angulo
    modX = np.abs(X)
    phasX = np.angle(X)
    phasX[modX < 0.00001] = 0

    ax[0].stem(W, modX)
    ax[0].set_title('Plot da FS de Vs(t) -> |X[k]|')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('w')
    ax[0].grid(True)

    ax[1].stem(W, phasX)
    ax[1].set_title('Plot da FS de Vs(t) -> Angle X[k]')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('w')
    ax[1].grid(True)

    #################################################################

    # figura 2 RC = 0.01
    fig1, ax1 = plt.subplots(3, 1, figsize=(8, 8))

    RC = 0.01
    H = 1 / (1 + (j * W * w0 * RC))
    Y1 = H * X
    y1 = ifft(Y1) * len(xs)
    y1 = np.real(y1)

    # modulo e fase
    modY1 = np.abs(Y1)
    phasY1 = np.angle(Y1)
    phasY1[modY1 < 0.00001] = 0

    #PLOTS
    ax1[0].plot(t, y1)
    ax1[0].set_title('y(t) com RC = 0.01s')
    ax1[0].set_ylabel('amp')
    ax1[0].set_xlabel('t')
    ax1[0].grid(True)

    ax1[1].stem(W, modY1)
    ax1[1].set_title('|Y1[k]|')
    ax1[1].set_ylabel('amp')
    ax1[1].set_xlabel('t')
    ax1[1].grid(True)

    ax1[2].stem(W, phasY1)
    ax1[2].set_title('angle|Y1[k]|')
    ax1[2].set_ylabel('amp')
    ax1[2].set_xlabel('t')
    ax1[2].grid(True)

    #################################################################

    # figura 3, RC = 0.1
    fig2, ax2 = plt.subplots(3, 1, figsize=(8, 8))
    RC = 0.1
    H = 1 / (1 + (j * W * w0 * RC))
    Y2 = H * X
    y2 = ifft(Y2) * len(xs)
    y2 = np.real(y2)

    # modulo e fase
    modY2 = np.abs(Y2)
    phasY2 = np.angle(Y2)
    phasY2[modY2 < 0.00001] = 0

    #PLOTS
    ax2[0].plot(t, y2)
    ax2[0].set_title('y2(t) com RC = 0.1s')
    ax2[0].set_ylabel('amp')
    ax2[0].set_xlabel('t')
    ax2[0].grid(True)

    ax2[1].stem(W, modY2)
    ax2[1].set_title('|Y2[k]|')
    ax2[1].set_ylabel('amp')
    ax2[1].set_xlabel('t')
    ax2[1].grid(True)

    ax2[2].stem(W, phasY2)
    ax2[2].set_title('angle|Y2[k]|')
    ax2[2].set_ylabel('amp')
    ax2[2].set_xlabel('t')
    ax2[2].grid(True)

    #################################################################

    # figura 4, RC = 1
    fig3, ax3 = plt.subplots(3, 1, figsize=(8, 8))
    RC = 1
    H = 1 / (1 + (j * W * w0 * RC))
    Y3 = H * X
    y3 = ifft(Y3) * len(xs)
    y3 = np.real(y3)

    # modulo e fase
    modY3 = np.abs(Y3)
    phasY3 = np.angle(Y3)
    phasY3[modY3 < 0.00001] = 0

    # PLOTS
    ax3[0].plot(t, y3)
    ax3[0].set_title('y3(t) com RC = 1s')
    ax3[0].set_ylabel('amp')
    ax3[0].set_xlabel('t')
    ax3[0].grid(True)

    ax3[1].stem(W, modY3)
    ax3[1].set_title('|Y3[k]|')
    ax3[1].set_ylabel('amp')
    ax3[1].set_xlabel('t')
    ax3[1].grid(True)

    ax3[2].stem(W, phasY3)
    ax3[2].set_title('angle|Y3[k]|')
    ax3[2].set_ylabel('amp')
    ax3[2].set_xlabel('t')
    ax3[2].grid(True)

    fig.tight_layout()
    plt.show()

main()