'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np

def main():

    fig, ax = plt.subplots(3, 1)
    fig2, ax2 = plt.subplots(3, 1)

    t = np.arange(0, 4, .001)

    # vi(t)
    vi = np.cos(np.pi * t)
    ax[0].plot(t, vi)
    ax[0].set_title('vi(t)')
    ax[0].set_ylabel('amp')
    ax[0].set_xlabel('n')
    ax[0].set_xlim(0, 4)
    ax[0].grid(True)

    # funcao que retorna vo(t)
    def sinalVo(x, t):
        v = []
        for i in range(len(t)):
            if(x[i] > 0.5):
                v.append(0.5)
            if(x[i] < -0.5):
                v.append(-0.5)
            else:
                v.append(x[i])
        return v

    vo = sinalVo(vi, t)
    t2 = np.arange(0, 5.334, .001)
    ax[1].plot(t2, vo)
    ax[1].set_title('vo(t)')
    ax[1].set_ylabel('amp')
    ax[1].set_xlabel('n')
    ax[1].set_xlim(0, 4)
    ax[1].grid(True)

    ax2[0].plot(t, 0.3*vi)
    ax2[0].set_title('0.3 * vi(t)')
    ax2[0].set_ylabel('amp')
    ax2[0].set_xlabel('n')
    ax2[0].set_xlim(0, 4)
    ax2[0].grid(True)

    ax2[1].plot(t, sinalVo(0.3*vi, t))
    ax2[1].set_title('0.3 * vo(t)')
    ax2[1].set_ylabel('amp')
    ax2[1].set_xlabel('n')
    ax2[1].set_xlim(0, 4)
    ax2[1].grid(True)

    ax[2].text(0.5, 0.5, 'O sistema não é linear e não é invariante no tempo.', horizontalalignment='center', verticalalignment='center')
    ax2[2].text(0.5, 0.5, 'O sistema não é linear e é invariante no tempo.', horizontalalignment='center', verticalalignment='center')

    fig.tight_layout()
    plt.show()

main()