import numpy as np
from matplotlib.pyplot import *
from sklearn.linear_model import LinearRegression
import pandas as pd

gas_flow_rate = np.array([2, 2.5, 3, 3.5, 4])
height_of_flame = np.array([3.4, 3.93, 4.32, 6.91, 6.90])
data = pd.DataFrame({'gas_flow_rate': [2, 2.5, 3, 3.5, 4],
                     'height_of_flame': [3.4, 3.93, 4.32, 6.91, 6.90]})
train_data = np.array(data['gas_flow_rate']).reshape(data['gas_flow_rate'].shape[0],
                                                     1)  # looking at it as a column_2D_array
text_data = np.array(data['height_of_flame']).reshape(data['height_of_flame'].shape[0], 1)
reg = LinearRegression();
md = reg.fit(train_data, text_data)  # building linear_regression model
y = md.predict(train_data)
B0 = md.intercept_;
B1 = md.coef_
figure, ax1 = subplots(nrows=1, ncols=1)
ax1.set_xlim(1, 5)
ax1.set_ylim(2, 8)
ax1.scatter(gas_flow_rate, height_of_flame, lw=2, c='b',label='scatter-point')

ax1.set_xlabel('$gas-flow-rate-L/h$')
ax1.set_ylabel('$height-of-diffusion-flame-cm$')
ax1.set_title('$the-relations-between-height-of-flame-and-gas-flow-rate$')
ax1.plot(gas_flow_rate, y, ls='--', lw=3, c='y',label='linear-result')
ax1.legend(loc='lower right')
savefig('Figure_combustion', dpi=500)
show()
R2 = reg.score(text_data, y)
print('截距是：', B0)
print('回归系数是： ', B1)
print('R^2(拟合优度）：', R2)
