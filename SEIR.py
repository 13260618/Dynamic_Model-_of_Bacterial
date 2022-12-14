import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


N = 100000
I0, E0, R0= 0, 20,2.68
S0 = N
beta, gamma,lambd = 1, 0.2, 0.142
t = np.linspace(0, 120, 120)

# Ecuaciones diferenciales del modelo
def deriv(y, t, N, beta, gamma,lambd):
    S,E, I, R = y
    dS = -beta * S * I / N
    dE = beta * S * I/N-lambd * E
    dI = lambd * E - gamma * I
    dR = gamma * I
    return dS, dE,dI, dR


y0 = S0, E0,I0, R0
ret = odeint(deriv, y0, t, args=(N, beta, gamma,lambd))  #integración con el método ODE en el intervalo t
S,E, I, R = ret.T

# Gráficos de S(t), I(t) y R(t)
fig = plt.figure()
ax = fig.add_subplot(111, axisbelow=True)
ax.plot(t, S/1000,  alpha=0.5, lw=1.5, label='S')
ax.plot(t, E/1000,  alpha=0.5, lw=1.5, label='E')
ax.plot(t, I/1000,  alpha=0.5, lw=1.5, label='I')
ax.plot(t, R/1000,  alpha=0.5, lw=1.5, label='R')
ax.set_xlabel('Días',fontsize = 12)
ax.set_ylabel('Población (miles)',fontsize = 12)
plt.title("Predicciones del modelo SEIR con Python",fontsize = 14)
legend = ax.legend()
plt.show()
