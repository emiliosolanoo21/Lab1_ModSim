import numpy as np
import matplotlib.pyplot as plt

def dP_dt(P, t):
    return 0.0004 * P**2 - 0.06 * P

# Método de Runge-Kutta de orden 4
def rk4(f, P0, t):
    n = len(t)
    P = np.zeros(n)
    P[0] = P0
    for i in range(1, n):
        h = t[i] - t[i-1]
        k1 = h * f(P[i-1], t[i-1])
        k2 = h * f(P[i-1] + 0.5 * k1, t[i-1] + 0.5 * h)
        k3 = h * f(P[i-1] + 0.5 * k2, t[i-1] + 0.5 * h)
        k4 = h * f(P[i-1] + k3, t[i-1] + h)
        P[i] = P[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
    return P

P0_d = 200
P0_e = 100

t = np.linspace(0, 50, 10000)

P_d = rk4(dP_dt, P0_d, t)
P_e = rk4(dP_dt, P0_e, t)

plt.figure(figsize=(10, 6))
plt.plot(t, P_d, label='P(0) = 200', color='blue')
plt.plot(t, P_e, label='P(0) = 100', color='green')
plt.axhline(y=150, color='red', linestyle='--', label='Punto de equilibrio P = 150')
plt.ylim(0, 300)  # Ajustamos el límite del eje y para evitar la escala exponencial
plt.xlabel('Tiempo (semanas)')
plt.ylabel('Población P(t)')
plt.title('Comportamiento de la población P(t) en el tiempo')
plt.legend()
plt.grid(True)
plt.show()
