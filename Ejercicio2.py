
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y1 = x**2 + 1
y2 = x**2 - 3
y3 = x**2
y4 = x**2 - 3  

plt.plot(x, y1, label='y(1) = 2: y = x^2 + 1')
plt.plot(x, y2, label='y(1) = -2: y = x^2 - 3')
plt.plot(x, y3, label='y(1) = 1: y = x^2')
plt.plot(x, y4, label='y(0) = -3: y = x^2 - 3', linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Soluciones de la EDO')
plt.legend()
plt.grid(True)
plt.show()
