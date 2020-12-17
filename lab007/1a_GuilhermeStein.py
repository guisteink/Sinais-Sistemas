'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift

#lab007 exercicio 1a

# criando o vetor de tempo e definindo a frequencia de amostragem
wam = 30
Tam = 2*np.pi / wam
t = np.arange(-10, 10, Tam)
cont = 0
N = pow(2, 12)

def rampa_unit(cont):
    x = np.arange(-10, 10, Tam)
    y = np.arange(-10, 10, Tam)
    z = np.arange(-10, 10, Tam)

    cont = 0
    for i in range(len(x)):
        if(x[i] < -5):
            x[i] = 0
        else:
            x[i] = cont
            cont += Tam

    cont = 0
    for j in range(len(y)):
        if (y[j] < 0):
            y[j] = 0
        else:
            y[j] = cont
            cont += Tam

    cont = 0
    for k in range(len(z)):
        if(z[k] < 5):
            z[k] = 0
        else:
            z[k] = cont
            cont += Tam

    return x - 2*y + z

##############################################################################################################

# sinal x(t) modulante
corrige_amplitude = 0.2
x = corrige_amplitude * (0.2 * rampa_unit(cont))

# transformada continua
Xjw = (Tam*N)*fft(x,N)/N
jw = fftfreq(len(Xjw), d=Tam * 2*np.pi)

# posicionando a frequencia 0 no meio do gráfico
Wd = fftshift(jw)
Xd = fftshift(Xjw)

# magnitude de Xjw
modXjw = np.abs(Xd)

fig, ax = plt.subplots(2, figsize=(10,6))

# plot de x(t)
ax[0].plot(t, x)
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("Tempo, em s")
ax[0].set_title("x(t)")

# plot de magnitude
ax[1].plot(Wd, modXjw)
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("Frequência (rad/s)")
ax[1].set_title("Magnitude de X(jw)")


##############################################################################################################

fig.tight_layout()
plt.show()