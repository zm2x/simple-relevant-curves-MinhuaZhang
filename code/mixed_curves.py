import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

t = np.array([i for i in range(0, 26, 2)])
temp = np.array([25.6, 59.55, 68.3, 93.8, 86.7, 74.6, 76.4, 92.5, 81.7, 91.5, 92.0, 92.5, 90.0])
# a = np.size(temp)
# print(a)
figure, axis = plt.subplots(nrows=1, ncols=1)
axis.plot(t, temp, ls='-', lw=2, c='b', label='furnace_temp=150')
x_smooth = np.linspace(t.min(), t.max(), 300)
y_smooth = make_interp_spline(t, temp)(x_smooth)
axis.plot(x_smooth, y_smooth, ls='-', lw=2, c='r', label='furnace_temp=150/spline')
axis.set_xlabel('$time/s$')
axis.set_ylabel('$temperature-of-component-surface/degree$')
axis.set_xlim(0, 25)
axis.set_title('$the-variant-temperature-of-component-surface$')
plt.legend()
plt.savefig('fixed_curves', dpi=500)
plt.show()

