import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(x, y):
    return (x - 3*y - 3*(x**2 - y**2) + 3*x*y) / (2*x - y + 3*(x**2 - y**2) + 2*x*y)

# Campo de direcciones
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
U = 1
V = f(X, Y)
fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
sol = solve_ivp(f, [1.5, 2], [0], dense_output=True)
t = np.linspace(1.5, 2, 100)
y_sol = sol.sol(t)
ax.plot(t, y_sol[0], 'r', label='Solución y(1.5) = 0')
ax.legend()
plt.title('Campo de direcciones y solución de la EDO')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
