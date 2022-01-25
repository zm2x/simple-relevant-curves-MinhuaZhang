import numpy as np
from matplotlib.pyplot import *

t = np.linspace(0, 200, 1000);
tao = np.array([49.5, 57.5, 21]);
T0 = np.array([29.25, 31.65, 24.19]);
Te = np.array([51.17, 49.91, 50.5]);
figure, axis = subplots(nrows=2, ncols=2);
axis[0][0].set_title('$dynamic-response-constant$')
T1 = T0[0] + (Te[0] - T0[0]) * (1 - np.exp(-t / tao[0]));
T2 = T0[1] + (Te[1] - T0[1]) * (1 - np.exp(-t / tao[1]));
T3 = T0[2] + (Te[2] - T0[2]) * (1 - np.exp(-t / tao[2]));
axis[0][0].plot(t, T1, lw=2.5, ls='-', c='r',label='$thermal-couple$');
axis[0][0].set_ylabel('$temperature$');

axis[0][1].plot(t, T2, lw=3, ls=':', c='blue',label='$thermal-resistance$');
axis[1][0].plot(t, T3, lw=3, ls='-', c='black',label='$variant-component$');
axis[1][0].set_ylabel('$temperature$');
axis[1][0].set_xlabel('$time/s$');


show()
savefig('dynamic-response', dpi=500);
