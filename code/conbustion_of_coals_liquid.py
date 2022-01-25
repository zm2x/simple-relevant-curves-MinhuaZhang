import numpy as np
import matplotlib.pyplot as plt

temp0 = np.array(
    [54, 63, 74, 86, 110, 127, 170, 222, 291, 363, 446, 501, 548, 597, 628, 657, 679, 692, 698, 700, 702, 701, 600]);

time0 = np.array([i for i in range(0, 3 * np.size(temp0), 3)]);
temp1 = np.array(
    [469, 487, 505, 516, 532, 544, 552, 558, 566, 570, 575, 580, 585, 590, 595, 599, 603, 606, 609, 611, 613, 616, 618,
     619,
     621, 623, 624, 625, 626, 626, 626, 626, 627, 626, 600]);
time1 = np.array([j for j in range(0, 3 * np.size(temp1), 3)]);
figure, axis = plt.subplots(nrows=2, ncols=1);
fig1, = axis[0].plot(time0, temp0, ls='-', lw=2, c='g', label='$d=4mm$');
fig2, = axis[1].plot(time1, temp1, ls='-', lw=2, c='r', label='$d=6mm$');
axis[0].legend(handles=[fig1],loc='lower right');
axis[1].legend(handles=[fig2],loc='lower right');
axis[0].set_ylabel('$temperature-of-liquid-coals$');
axis[1].set_xlabel('$time/s$')
axis[0].set_title('$variant-temperature-of-liquid-coals-in-variant-times$');

plt.show();
