from __future__ import division
import numpy as np

# Amount of time in minutes I spend shoehorning memes from 2008 I just discovered into the lecture's slide deck

X = np.array([8, 15,  22, 1,   35]).reshape(5, 1)

# Quality of the lecture
y = np.array([8, 7.8, 4,  9.4, 3]).reshape(5, 1)

import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt

plt.scatter(X, y)
plt.title('Quality of lectures regressed onto the proportion of prep time spent shoehorning memes into the slide deck')
plt.ylabel('Quality of lecture')
plt.xlabel('Proportion of prep time spent shoehorning memes into the slide deck')
plt.xlim(0, 50)
# plt.show()

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)
print 'beta', regressor.coef_
print 'alpha', regressor.intercept_

# calc variance of x, covariance of x and y
# calc b
# calc a

# x - xbar ** 2 / n -1
xbar = np.mean(X)
print 'xbar', xbar
var = ((X[0] - xbar)**2 + (X[1] - xbar)**2 + (X[2] - xbar)**2 + (X[3] - xbar)**2 + (X[4] - xbar)**2) / 4
print 'var', var
# x - xbar y - ybar / 4
ybar = np.mean(y)
print 'ybar', ybar
cov = ( (X[0] - xbar)*(y[0] - ybar)
        + (X[1] - xbar)*(y[1] - ybar)
        + (X[2] - xbar)*(y[2] - ybar)
        + (X[3] - xbar)*(y[3] - ybar)
        + (X[4] - xbar)*(y[4] - ybar) ) / 4
print 'cov', cov
beta = cov / var
print 'beta', beta
print 'alpha', ybar - beta * xbar

alpha = ybar - beta * xbar

print alpha + beta * 11
print alpha + beta * 10
print alpha + beta * 3
print alpha + beta * 24


X_test = np.array([11, 10, 3, 24]).reshape(4, 1)
y_test = np.array([7.9, 7.2, 9.2, 4]).reshape(4, 1)

print regressor.score(X_test, y_test)