import numpy as np

import matplotlib.pyplot as plt

M = 200000

def weierstrass(x, N):
	y = np.zeros((1,M))
	for n in range(1,N):

		y = y + np.cos(3**n*np.pi*x)/2**n
	return y

x = np.linspace(-2,2,M)

y = np.reshape(weierstrass(x,500),(M,))

plt.grid(True)

plt.plot(x, y, 'r-')
plt.title("Weierstrass Function")

plt.show()
