import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 23, 24)
y = np.array(
    [233, 360, 430, 424, 339, 287, 262, 309, 417, 535, 608, 552, 161, 335, 458, 529, 485, 411, 365, 374, 414, 508, 636,
     548])

figure, ax = plt.subplots(nrows=2, ncols=1)

colordistribution = ['r', 'b', 'g', 'r', 'y', 'r', 'b', 'g', 'r', 'y', 'r', 'b', 'g', 'r', 'y', 'r', 'b', 'g', 'r',
                     'y', 'r', 'b', 'g', 'r']
square = x * 4;
ax[0].scatter(x, y, s=square, marker='*', c=colordistribution)
ax[0].set_xlabel('$x/mm$');
ax[0].set_ylabel('$temperature$');
ax[0].set_title('$scatter-and-continuous-diagram-of-flame-temperature-distribution$',fontsize=11);
ax[1].plot(x, y, ls='-', lw=2, c='r')
ax[1].set_xlabel('$x/mm$',labelpad=2.0)
ax[1].set_ylabel('$temperature$',labelpad=2.5);
plt.savefig('Figure_flame_temperature_distribution', dpi=500)
plt.show();

