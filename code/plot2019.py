import numpy as np
import matplotlib.pyplot as plt


gas_flow_rate = np.array([2, 2.5, 3, 3.5, 4]);
height_of_flame = np.array([3.4, 3.93, 4.32, 6.91, 6.90])
fig = plt.Figure(figsize=(8, 6), dpi=500)


plt.plot(gas_flow_rate, height_of_flame, ls='-', lw=2, color='g')
plt.text(2,3.4,'(2,3.4)',size=15,color='r')
plt.text(2.5,3.93,'(2.5,3.93)',size=15,color='b')
plt.text(3,4.32,'(3,4.32)',size=15,color='y')
plt.text(3.5,6.91,'(3.5,6.91)',size=15,color='r')

plt.title('$the-relations-between-height-of-flame-and-gas-flow-rate$')
plt.xlabel('$gas-flow-rate-L/h$')
plt.ylabel('$height-of-diffusion-flame-cm$')
plt.xlim(1, 5)
plt.ylim(2, 8)

plt.show()
plt.savefig('fig_avail', dpi=500)
