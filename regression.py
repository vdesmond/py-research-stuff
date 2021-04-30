#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

np.random.seed(1)
# n = 100
# b0 = 5
# b1 = 2
# x = 10 * ss.uniform.rvs(size=n)
# y = b0 + b1 * x + ss.norm.rvs(loc=0, scale=1, size=n)

# plt.figure()
# plt.plot(x, y, "o", ms=5)
# xx = np.array([0, 10])
# plt.plot(xx, b0 + b1 * xx)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

# print(np.mean(x))
# print(np.mean(y))


def compute_rss(y_estimate, y):
    return sum(np.power(y - y_estimate, 2))


def estimate_y(x, b_0, b_1):
    return b_0 + b_1 * x


# rss = compute_rss(estimate_y(x, b0, b1), y)

# rsslist = []
# slopes = slopes = np.arange(-10, 15, 0.001)
# for slope in slopes:
#     rsslist.append(compute_rss(estimate_y(x, b0, slope), y))
# plt.plot(slopes, rsslist)
# ind_min = np.argmin(rsslist)
# plt.scatter(slopes[ind_min], rsslist[ind_min])
# plt.show()

# print("Estimated slope = ", slopes[ind_min])


# X = sm.add_constant(x)
# model = sm.OLS(y, X)
# est = model.fit()
# print(est.summary())

# Multilinear regression

# n = 1000
# b0 = 5
# b1 = 2
# b2 = -1
# x1 = 10 * ss.uniform.rvs(size=n)
# x2 = 10 * ss.uniform.rvs(size=n)
# y = b0 + (b1 * x1) + (b2 * x2) + ss.norm.rvs(loc=0, scale=4, size=n)

# X = np.stack([x1, x2], axis=1)


# fig = plt.figure()
# ax = fig.add_subplot(111, projection="3d")
# ax.scatter(X[:, 0], X[:, 1], y, c=y)
# ax.set_xlabel("x1")
# ax.set_ylabel("x2")
# ax.set_zlabel("y")

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, train_size=0.5, random_state=1
# )
# lm = LinearRegression(fit_intercept=True)
# lm.fit(X_train, y_train)
# print(lm.score(X_test, y_test))
# planex = np.linspace(0, 10, 10)
# planey = np.linspace(0, 10, 10)
# planeX, planeY = np.meshgrid(planex, planey)
# planeZ = lm.intercept_ + (planeX * lm.coef_[0]) + (planeY * lm.coef_[1])
# ax.plot_surface(planeX, planeY, planeZ, alpha=0.8)
# plt.show()
# print(lm.coef_[0], lm.coef_[1], lm.intercept_)

# Classification


def gen_data(n, h, sd1, sd2):
    x1 = ss.norm.rvs(-h, sd1, n)
    y1 = ss.norm.rvs(3, sd1, n)

    x2 = ss.norm.rvs(h, sd2, n)
    y2 = ss.norm.rvs(-1, sd2, n)
    return x1, y1, x2, y2


n = 1000
x1, y1, x2, y2 = gen_data(n, 2, 1.5, 2)
# plt.figure()
# plt.plot(x1, y1, "o", ms=2)
# plt.plot(x2, y2, "o", ms=2)
# plt.xlabel("$x_1$")
# plt.ylabel("$x_2$")
# plt.show()


# def prob_to_odds(p):
#     if p <= 0 or p >= 1:
#         print("Probabilities must be between 0 and 1.")
#     return p / (1 - p)

clf = LogisticRegression()
X = np.vstack((np.vstack((x1, y1)).T, np.vstack((x2, y2)).T))
y = np.hstack((np.repeat(1, n), np.repeat(2, n)))
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.5, random_state=1
)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))


def plot_probs(ax, clf, class_no):
    xx1, xx2 = np.meshgrid(np.arange(-10, 10, 0.1), np.arange(-10, 10, 0.1))
    probs = clf.predict_proba(np.stack((xx1.ravel(), xx2.ravel()), axis=1))
    Z = probs[:, class_no]
    Z = Z.reshape(xx1.shape)
    CS = ax.contourf(xx1, xx2, Z)
    cbar = plt.colorbar(CS)
    plt.xlabel("$X_1$")
    plt.ylabel("$X_2$")


plt.figure(figsize=(5, 8))
ax1 = plt.subplot(111)
ax1.scatter(np.stack([x1, x2]), np.stack([y1, y2]))
# plot_probs(ax1, clf, 0)
plt.title("Pred. prob for class 1")
# ax2 = plt.subplot(212)
# plot_probs(ax2, clf, 1)
# plt.title("Pred. prob for class 2")
plt.show()
