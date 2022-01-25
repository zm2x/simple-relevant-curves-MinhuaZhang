import numpy as np
import matplotlib.pyplot as plt

r = 1.41;
M = np.linspace(0.1, 2.0, 40)
figure, axs = plt.subplots(nrows=1, ncols=1)

for i in range(0, 40):
    belta = np.linspace(0.1, np.pi / 2, 500);
    selta = np.arctan(
        2 / np.tan(belta) *
        (np.square(M[i]) * np.square(np.sin(belta)) - 1) / (np.square(M[i]) * (r + np.cos(2 * belta)) + 2))

    belta = belta * 180 / np.pi
    selta = selta * 180 / np.pi
    plt.plot(selta, belta, ls='-', lw=0.4, c='black')

M0 = np.linspace(2.0, 10, 40)
for j in range(0, 40):
    belta = np.linspace(0.1, np.pi / 2, 500)
    selta = np.arctan(
        2 / np.tan(belta) *
        (np.square(M0[j]) * np.square(np.sin(belta)) - 1) / (np.square(M0[j]) * (r + np.cos(2 * belta)) + 2))
    belta = belta * 180 / np.pi
    selta = selta * 180 / np.pi
    plt.plot(selta, belta, ls='-', lw=0.4, c='r')


plt.xlim(0, 50)
plt.ylim(0, 90)
plt.xlabel('$deflaction-angle-selta-degrees$')
plt.ylabel('$shock-wave-angle-belta-degrees$')
plt.title('$Oblique-shockwave-properties,selta-belta-M-diagram$')
plt.annotate('$Ma1-rises$', xy=(35, 10), xytext=(2, 10), arrowprops=dict(facecolor='black', shrink=0.05))
plt.savefig('selta-belta-M-relation-curve',dpi=500)
plt.show()
