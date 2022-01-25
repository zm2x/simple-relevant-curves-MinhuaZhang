import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.interpolate import interp1d, make_interp_spline


# # define user function
def carbon_comsumption(timef=None, time=None, conf=None, con=None):
    carbon_com = 1200 * 0.001 * 0.01 * 12.017 / 60 / 22.414 * (conf + con) * 0.5 * (time - timef) * 1000;
    return carbon_com;


def concentration00(series=None):
    conresult = (series.values - np.ones(series.size) * 1.02E-09) / (2.53E-07 - 1.02E-09) * 0.101 * 100;
    return conresult;


def reshape(data0=None):
    return data0.reshape(-1, 1);


# # import data and preprocessing
# # key points:data can be selected using slice(dataframe.iloc())
standard = pd.read_csv(os.path.abspath('12.21.csv'));
eight_hund_temp = pd.read_csv(os.path.abspath('1-1-800.csv'));
# print(eight_hund_temp.head());
seven_hund_temp = pd.read_csv(os.path.abspath('1-2-700.csv'));
six_hund_temp = pd.read_csv(os.path.abspath('1-3-600.csv'));
eight_hund_temp = eight_hund_temp.drop(index=0);
eight_hund_temp = eight_hund_temp.reset_index(drop=True);
# print(eight_hund_temp.head(6));
seven_hund_temp = seven_hund_temp.drop(index=0);
seven_hund_temp = seven_hund_temp.reset_index(drop=True);
six_hund_temp = six_hund_temp.drop(index=0);
standard.plot(x='OFFSET', y='Trend [CO2]', c='r', ls=':', label='Trend of response');
plt.xlabel('$time/s$', fontsize=15);
plt.ylabel('$response-result$', fontsize=15)
plt.title('$variant-response-diagram$', fontsize=20)
plt.legend(fontsize=15);
plt.show();

# # compute concentration of carbon dioxide
series0 = eight_hund_temp['Trend [CO2]'];
con0 = series0.values;
series00 = eight_hund_temp['OFFSET'];
time0 = series00.values
series1 = seven_hund_temp['Trend [CO2]'];
con1 = series1.values;
series11 = seven_hund_temp['OFFSET'];
time1 = series11.values;
series2 = six_hund_temp['Trend [CO2]'];
con2 = series2.values;
series22 = six_hund_temp['OFFSET'];
time2 = series22.values;
concentration0 = concentration00(series0);
concentration1 = concentration00(series1);
concentration2 = concentration00(series2);

# # generate interpolate function and plotting
fig1, axis = plt.subplots(nrows=1, ncols=1, figsize=(20, 20));
x0 = np.linspace((series00.values[15:50] - 23.837).min(), (series00.values[15:50] - 23.837).max(), 200)
y0 = interp1d(series00.values[15:50] - 23.837, concentration0[15:50], kind='quadratic');
x1 = np.linspace((series11.values[62:100] - 96.5).min(), (series11.values[62:100] - 98.186).max(), 200);
y1 = interp1d(series11.values[62:100] - 96.5, concentration1[62:100], kind='quadratic');
x2 = np.linspace((series22.values[34:70] - 50.7).min(), (series22.values[34:70] - 53.194).max(), 200);
y2 = interp1d(series22.values[34:70] - 50.7, concentration2[34:70], kind=2);
axis.plot(x0, y0(x0), ls='-', c='b', lw=3, label='800K');
axis.plot(x1, y1(x1), ls='-', c='r', lw=3, label='700K');
axis.plot(x2, y2(x2), ls='-.', c='g', lw=3, label='600K');
axis.set_xlabel('$time/s$', fontsize=25, labelpad=1.5);
axis.set_ylabel('$concentration-of-carbon-dioxide/%$', fontsize=27, labelpad=2);
axis.set_title('$concentration-distribution-diagram$', fontsize=30);
plt.legend(fontsize=25);
plt.xlim(0, 50);
x_tick = range(0, 55, 5);
y_tick = range(0, 35, 5);
plt.xticks(x_tick, fontsize=15);
plt.yticks(y_tick, fontsize=15);
plt.savefig('concentration.png', dpi=600);
plt.show();

# #carbon reversion generation
list0 = [];
list1 = [];
list2 = [];
a0 = 0;
a1 = 0;
a2 = 0;
for i in range(1, time0.size, 1):
    a0 = a0 + carbon_comsumption(time0[i - 1], time0[i], con0[i - 1], con0[i])
    list0.append(a0);
    if i == time0.size - 1:
        total_com0 = a0;
reversion_rate0 = list0 / total_com0;
# a0 can be used in front session because a0 is the final iterable result when breaking iteration

for j in range(1, time1.size, 1):
    a1 = a1 + carbon_comsumption(time1[j - 1], time1[j], con1[j - 1], con1[j]);
    list1.append(a1);
    if j == time1.size - 1:
        total_com1 = a1;
reversion_rate1 = list1 / total_com1;
# print(len(list1));

for k in range(1, time2.size, 1):
    a2 = a2 + carbon_comsumption(time2[k - 1], time2[k], con2[k - 1], con2[k])
    list2.append(a2);
    if k == time2.size - 1:
        total_com2 = a2;
reversion_rate2 = list2 / total_com2;

# # plotting reversion curves
# fun0 = np.polyfit(time0[15:50] - 23.837, reversion_rate0[14:49], 2);
# x0 = np.linspace(time0[15] - 23.837, time0[50] - 23.837, 200);
# y0 = np.polyval(fun0, x0);
# fun1 = np.polyfit(time1[62:100] - 98.186, reversion_rate1[61:99], 2);
# x1 = np.linspace(time1[62] - 98.186, time1[100] - 98.186, 200);
# y1 = np.polyval(fun1, x1);
fig2, axis = plt.subplots(nrows=1, ncols=1, figsize=(15, 15));
x00 = np.linspace(time0[15] - 23.837, time0[50] - 23.837, 200);
y00 = interp1d(time0[5:60] - 23.837, reversion_rate0[4:59], kind=3);
x11 = np.linspace(time1[62] - 96.5, time1[100] - 98.186, 200);
y11 = interp1d(time1[30:102] - 96.5, reversion_rate1[29:101], kind=3);
x22 = np.linspace(time2[34] - 50.7, time2[70] - 53.194, 200);
y22 = interp1d(time2[15:80] - 50.7, reversion_rate2[14:79], kind=3);
axis.plot(x00, y00(x00), ls='-', c='b', lw=3, label='800K');
axis.plot(x11, y11(x11), ls='-', c='r', lw=3, label='700K');
axis.plot(x22, y22(x22), ls='-', c='y', lw=3, label='600K');
plt.xlabel('time/s', labelpad=2.0, fontsize=20);
plt.ylabel('$reversion-rate-of-carbon$', labelpad=2.0, fontsize=20);
plt.title('$reversion-rate-curves$', fontsize=30, pad=3.0);
x_tick0 = range(0, 60, 5);
y_tick0 = np.linspace(0, 1, 11);
plt.xticks(x_tick0, fontsize=15);
plt.yticks(y_tick0, fontsize=15);
plt.legend(fontsize=20, loc='lower right');
plt.savefig('reversion-rate-curves', dpi=600);
plt.show();

# # reversion velocity computation and plotting
fig3, axis = plt.subplots(nrows=1, ncols=1, figsize=(20, 20))
vel0 = np.diff(reversion_rate0) / np.diff(time0[1:]);
vel1 = np.diff(reversion_rate1) / np.diff(time1[1:]);
vel2 = np.diff(reversion_rate2) / np.diff(time2[1:]);
vel00 = np.diff(reversion_rate0[14:49]) / np.diff(time0[15:50]);
vel11 = np.diff(reversion_rate1[61:99]) / np.diff(time1[62:100]);
vel22 = np.diff(reversion_rate2[33:69]) / np.diff(time2[34:70]);
new_x0 = np.linspace(time0[17], time0[49], 500);
yy0 = interp1d(time0[16:50], vel00, kind=3);
new_y0 = yy0(new_x0);
plt.plot(new_x0 - 23.837, new_y0, ls='-', lw=3, c='g', label='800K');
new_x1 = np.linspace(time1[64], time1[99], 500)
yy1 = interp1d(time1[63:100], vel11, kind=3);
new_y1 = yy1(new_x1);
plt.plot(new_x1 - 96.5, new_y1, ls='-', lw=3, c='black', label='700K');
new_x2 = np.linspace(time2[36], time2[69], 500);
yy2 = interp1d(time2[35: 70], vel22, kind=3);
new_y2 = yy2(new_x2);
plt.plot(new_x2 - 50.7, new_y2, ls='-', lw=3, c='r', label='600K');
plt.xlabel('$time/s$', fontsize=15, labelpad=2.0);
axis.set_ylabel('$velocity-of-carbon-reversion$', fontsize=20, labelpad=2.0);
plt.title('$velocity-of-carbon-reversion$', fontsize=30, pad=3.0);
x_tick1 = range(0, 60, 5);
y_tick1 = np.linspace(0, 0.2, 21);
plt.xticks(x_tick1, fontsize=15);
plt.yticks(y_tick1, fontsize=15);
plt.legend(fontsize=15);
plt.show();

# # # attention:reversion of carbon must be monotone
fig4, axis = plt.subplots(nrows=1, ncols=1, figsize=(20, 18), sharex='all');
x_sm0 = np.linspace(reversion_rate0[16], reversion_rate0[48], 500)
y_sm0 = make_interp_spline(reversion_rate0[15:49], vel00)(x_sm0);
plt.plot(x_sm0, y_sm0, ls=':', lw=4, label='800K');
x_sm1 = np.linspace(reversion_rate1[63], reversion_rate1[98], 500);
y_sm1 = make_interp_spline(reversion_rate1[62:99], vel11)(x_sm1);
plt.plot(x_sm1, y_sm1, ls=':', lw=4, label='700K');
x_sm2 = np.linspace(reversion_rate2[35], reversion_rate2[68], 500);
y_sm2 = make_interp_spline(reversion_rate2[34:69], vel22)(x_sm2)
plt.plot(x_sm2, y_sm2, ls=":", lw=4, label='900K');
plt.xlabel('$reversion-rate$', fontsize=20, labelpad=2.0);
plt.ylabel('$velocity-of-reversion$', fontsize=20, labelpad=2.0);
plt.title('$relation-between-reversion/rate-and-reversion/velocity$', fontsize=30, pad=3.0);
plt.legend(fontsize=28, loc='upper left');
x_tick2 = np.linspace(0, 1, 11);
y_tick2 = np.linspace(0, 0.2, 11);
plt.xticks(x_tick2, fontsize=18);
plt.yticks(y_tick2, fontsize=18);
plt.legend(fontsize=15);
plt.savefig('velocity-conversion.png', dpi=600);
plt.show();

# # writing data to excel
# # the length of list can be different and axis would be transformed
# # transpose and reshape(rows,cols) would not have function in here
data = [time0, concentration0, reversion_rate0, vel0, time1, concentration1, reversion_rate1, vel1,
        time2,
        concentration2,
        reversion_rate2, vel2];
columns = ['800K/time1', 'CO2浓度', '碳转化率', '转化速率',
           '700K/time2', 'CO2浓度', '碳转化率', '转化速率',
           '600K/time3', 'CO2浓度', '碳转化率', '转化速率']

time0 = reshape(data[0]);
concentration0 = reshape(data[1]);
reversion_rate0 = reshape(data[2]);
vel0 = reshape(data[3]);
time1 = reshape(data[4]);
concentration1 = reshape(data[5]);
reversion_rate1 = reshape(data[6]);
vel1 = reshape(data[7]);
time2 = reshape(data[8]);
concentration2 = reshape(data[9]);
reversion_rate2 = reshape(data[10]);
vel2 = reshape(data[11]);
df = pd.DataFrame(data=data[0], columns=[columns[0]]);
for kk in range(1, 12, 1):
    df = pd.concat([df, pd.DataFrame(data=data[kk], columns=[columns[kk]])], axis=1)
# for kk in range(1, 12, 1):
#     df.insert(kk, column=columns[kk], value=data[kk]);

with pd.ExcelWriter(os.path.join(os.getcwd(), 'combustion_experiment_processed_data.xlsx')) as writer:
    df.to_excel(writer, sheet_name='数据后处理结果');
