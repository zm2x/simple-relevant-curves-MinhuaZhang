import numpy as np
import matplotlib.pyplot as plt

r = 1.412;
M1 = np.linspace(1, 10, 100)

p_ratio = 1 + 2 * r / (r + 1) * (np.power(M1, 2) - np.ones(100));
density_ratio = (r + 1) * np.power(M1, 2) / (2 + (r - 1) * np.power(M1, 2));
T_ratio = p_ratio / density_ratio;
M2 = np.sqrt((1 + (r - 1) / 2 * np.power(M1, 2)) / (r * np.square(M1) - (r - 1) / 2));
Cp = 1003.2;
R = 287.15;
delts = Cp * np.log(T_ratio) - R * np.log(p_ratio);
Po_ratio = np.exp((-1) * delts / R);
figure, axis1 = plt.subplots(nrows=1, ncols=1, figsize=(13, 13))
f2, = axis1.plot(M1, Po_ratio, ls='-', lw=2, c='m');
f1, = axis1.plot(M1, M2, ls='-', lw=2, c='r');

axis2 = axis1.twinx();
f3, = axis2.plot(M1, T_ratio, ls='--', lw=2, c='blue');
f4, = axis2.plot(M1, density_ratio, ls='--', lw=2, c='g');
f5, = axis2.plot(M1, p_ratio, ls='--', lw=2, c='black');
axis1.set_xlabel('$M1$', fontsize=15)
axis1.set_ylabel('$M2-and-P02/P01$', fontsize=15)
axis2.set_ylabel('$P2/P1,T2/T2and-density2/density1$', fontsize=15)
plt.title('$variation-properties-across-the-normal-shock-wave$', fontsize=15)
plt.annotate('M2', xy=(4, 8.8), xytext=(4.2, 16.0), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('P02/P01', xy=(2.2, 12.5), xytext=(3, 12.5), arrowprops=dict(facecolor='black', shrink=0.05))
axis1.set_ylim(0, 1)
axis1.set_xlim(1, 10)
axis2.set_ylim(0, 20)
plt.legend([f1, f2], ['M2', 'P02/P01'], loc='best')
plt.legend([f3, f4, f5], ['T2/T1', 'density1/density2', 'P2/P1'], loc='lower right', fontsize='medium')
plt.savefig('some_relevant_aerodynamics_curves', dpi=500)
plt.show()
# print('总压之比：',Po_ratio)
# print('马赫数M2:',M2)
