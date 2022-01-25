import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

r = 1.41;
a = []
b = []
M = np.linspace(0.1, 10.0, 500)
figure, axs = plt.subplots(nrows=1, ncols=1)
belta = np.linspace(0.01, np.pi / 2, 2000)
selta = np.linspace(0, np.pi / 4, 2000)
for i in range(0, 500):
    Mn2 = np.sqrt((1 + (r - 1) / 2 * np.power(M[i] * np.sin(belta), 2)) / (
            r * np.square(M[i] * np.sin(belta)) - (r - 1) / 2)) / np.sin(belta - selta)
    for j in range(0, 2000):

        if abs(Mn2[j] - 1) < 1e-4:
            a.append(belta[j])
            b.append(selta[j])
print(len(b))
print(len(a))
a = np.array(a)
b = np.array(b)
a = a * 180 / np.pi;
b = b * 180 / np.pi;
plt.plot(b, a, c='m')

plt.show()
print(b)
print('\n')
print(a)
print('\n')
