import numpy as np
from matplotlib.pyplot import *

lanmda = np.linspace(0, 3, 100)
k = 1.41
c = 1 - (k - 1) / (k + 1) * np.square(lanmda)
pi_lanmda = np.power(c, k / (k - 1))
q = lanmda * np.power((k + 1) / 2, 1 / (k - 1)) * np.power(c, 1 / (k - 1));
y = q / pi_lanmda;
figure, axis1 = subplots(nrows=1, ncols=1);
axis1.plot(lanmda, q, ls='-', lw=2, c='black')
axis2 = axis1.twinx()
axis2.plot(lanmda, y, ls='-', lw=4, c='red')
axis1.set_xlabel('$lanmda/coefficient-of-velocity$')
axis1.set_ylabel('$q/function-of-flow-rate$')
axis2.set_ylabel('$y(lanmda)$')
title('$the-distribution-of-q-and-y$')
axis1.set_xlim(0,2.8)
axis1.set_ylim(0,1)
axis2.set_ylim(0,5)
grid()

show()
savefig('velocity-curves',dpi=500)
