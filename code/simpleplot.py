#光滑曲线
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
x=np.linspace(1,5,1000)
gas_flow_rate = np.array([2, 2.5, 3, 3.5, 4]);
height_of_flame = np.array([3.4, 3.93, 4.32, 6.91, 6.90])
fig = plt.Figure(figsize=(8, 6), dpi=500)
model0 = make_interp_spline(gas_flow_rate,height_of_flame)
y=model0(x)
plt.plot(x, y, ls='-', lw=2, color='g')
plt.title('$the-relations-between-height-of-flame-and-gas-flow-rate$')
plt.xlabel('$gas-flow-rate-L/h$')
plt.ylabel('$height-of-diffusion-flame-cm$')
plt.xlim(1, 5)
plt.ylim(2, 8)
plt.savefig('fig_avail', dpi=500)
plt.show()

