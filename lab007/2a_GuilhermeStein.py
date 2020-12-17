'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift

#lab007 exercicio 2a

# essa função é igual a usada para os calculos porem com o heaviside no 0, para melhor visualizaçao no plot
def degrau2(t, d1, d2):
    u1 = np.arange(0, 5, Tam)
    for i in range(len(u1)):
        if u1[i] < d1:
            u1[i] = 0
        else:
            u1[i] = 1
    u1 = np.heaviside(t, Tam)

    u2 = np.arange(0, 5, Tam)
    for j in range(len(u2)):
        if u2[j] < d2:
            u2[j] = 0
        else:
            u2[j] = 1

    return (u1 - u2)

def degrau(t, d1, d2):
    u1 = np.arange(t[0], t[-1] + Tam, Tam)
    for i in range(len(u1)):
        if u1[i] < d1:
            u1[i] = 0
        else:
            u1[i] = 1

    u2 = np.arange(t[0], t[-1] + Tam, Tam)
    for j in range(len(u2)):
        if u2[j] < d2:
            u2[j] = 0
        else:
            u2[j] = 1

    return (u1 - u2)

fig, ax = plt.subplots(3, 3, figsize=(13,6))

##############################################################################################################
# a
# amostragem e vetor no tempo
wam = 500
Tam = 2*np.pi/wam
t = np.arange(0, 5, Tam)
N = pow(2, 12)

#sinal x1a
x1a = degrau(t, 0, 2)
x1a_2 = degrau2(t, 0, 2)

# calculo da FT e da frequencia
X1a = (Tam*N)*fft(x1a, N)/N
w1a = fftfreq(len(X1a), d=(Tam))*(2*np.pi)

# posicionando os zeros no meio
wd1a = fftshift(w1a)
Xd1a = fftshift(X1a)

# magnitude e fase da transformada FT
ModX1a = np.abs(Xd1a)
phasX1a = np.angle(Xd1a)

# plot da letra x1a
ax[0][0].plot(t, x1a_2, 'b-')
ax[0][0].set_ylabel("Amplitude")
ax[0][0].set_xlabel("Tempo, em s")
ax[0][0].set_title("[x1a] u(t)-u(t-2)")

# plot de magnitude
ax[0][1].plot(wd1a, ModX1a, 'b-')
ax[0][1].set_ylabel("Amplitude")
ax[0][1].set_xlabel("Frequencia, em rad/s")
ax[0][1].set_title("Magnitude de X1a")
ax[0][1].set_xlim(-150, 150)

# plot de fase
ax[0][2].stem(wd1a, phasX1a)
ax[0][2].set_ylabel("Amplitude")
ax[0][2].set_xlabel("Frequencia, em s")
ax[0][2].set_title("Fase de X1a")
ax[0][2].set_xlim(-100, 100)

##############################################################################################################
# b
# amostragem e vetor no tempo
wam = 2000
Tam = 2*np.pi/wam
t = np.arange(0, 5, Tam)
N = pow(2, 12)
# sinal x1b
x1b = degrau(t, 0, 1)
x1b_2 = degrau2(t, 0, 1)

# calculo da FT e da frequencia
X1b = (Tam*N)*fft(x1b, N)/N
w1b = fftfreq(len(X1b), d=(Tam))*(2*np.pi)

# posicionando os zeros no meio
wd1b = fftshift(w1b)
Xd1b = fftshift(X1b)

# magnitude e fase da transformada FT
ModX1b = np.abs(Xd1b)
phasX1b = np.angle(Xd1b)

# plot da letra x1b
ax[1][0].plot(t, x1b_2, 'r-')
ax[1][0].set_ylabel("Amplitude")
ax[1][0].set_xlabel("Tempo, em s")
ax[1][0].set_title("[x1b] u(t)-u(t-1)")

# plot de magnitude
ax[1][1].plot(wd1b, ModX1b, 'r-')
ax[1][1].set_ylabel("Amplitude")
ax[1][1].set_xlabel("Frequencia, em rad/s")
ax[1][1].set_title("Magnitude de X1b")
ax[1][1].set_xlim(-150, 150)

# plot de fase
ax[1][2].stem(wd1b, phasX1b)
ax[1][2].set_ylabel("Amplitude")
ax[1][2].set_xlabel("Frequencia, em s")
ax[1][2].set_title("Fase de X1b")
ax[1][2].set_xlim(-100, 100)



##############################################################################################################
# c
# amostragem e vetor no tempo
wam = 2000
Tam = 2*np.pi/wam
t = np.arange(0,5, Tam)
N = pow(2, 12)
# sinal x1c
x1c = degrau(t, 0, 0.35)
x1c_2 = degrau2(t, 0, 0.35)

# calculo da FT e da frequencia
X1c = (Tam*N)*fft(x1c, N)/N
w1c = fftfreq(len(X1c), d=(Tam))*(2*np.pi)

# posicionando os zeros no meio
wd1c = fftshift(w1c)
Xd1c = fftshift(X1c)

# magnitude e fase da transformada FT
ModX1c = np.abs(Xd1c)
phasX1c = np.angle(Xd1c)

# plot da letra x1c
ax[2][0].plot(t, x1c_2, 'g-')
ax[2][0].set_ylabel("Amplitude")
ax[2][0].set_xlabel("Tempo, em s")
ax[2][0].set_title("[x1c] u(t)-u(t-0.35)")

# plot de magnitude
ax[2][1].plot(wd1c, ModX1c, 'g-')
ax[2][1].set_ylabel("Amplitude")
ax[2][1].set_xlabel("Frequencia, em rad/s")
ax[2][1].set_title("Magnitude de X1c")
ax[2][1].set_xlim(-150, 150)

# plot de fase
ax[2][2].stem(wd1c, phasX1c)
ax[2][2].set_ylabel("Amplitude")
ax[2][2].set_xlabel("Frequencia, em s")
ax[2][2].set_title("Fase de X1c")
ax[2][2].set_xlim(-100, 100)


##############################################################################################################

fig.tight_layout()
plt.show()

