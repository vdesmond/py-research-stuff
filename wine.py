#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np, random, scipy.stats as ss
import pandas as pd
import sklearn.preprocessing
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages


def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode


def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))


def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]


def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]


wine_dataset = pd.read_csv("wine.csv")
wine_dataset["is_red"] = np.where(wine_dataset["color"] == "red", 1, 0)
numeric_data = wine_dataset.drop(["quality", "high_quality", "color"], 1)
scaled_data = sklearn.preprocessing.scale(numeric_data)
numeric_data = pd.DataFrame(data=scaled_data, columns=numeric_data.columns)
pca = PCA(n_components=2)
principal_components = pca.fit_transform(numeric_data)

# observation_colormap = ListedColormap(["red", "blue"])
# x = principal_components[:, 0]
# y = principal_components[:, 1]

# plt.title("Principal Components of Wine")
# plt.scatter(
#     x,
#     y,
#     alpha=0.2,
#     c=wine_dataset["high_quality"],
#     cmap=observation_colormap,
#     edgecolors="none",
# )
# plt.xlim(-8, 8)
# plt.ylim(-8, 8)
# plt.xlabel("Principal Component 1")
# plt.ylabel("Principal Component 2")
# plt.show()

np.random.seed(1)
x = np.random.randint(0, 2, 1000)
y = np.random.randint(0, 2, 1000)


def accuracy(predictions, outcomes):
    return 100 * np.mean(predictions == outcomes)


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(numeric_data, wine_dataset["high_quality"])
library_predictions = knn.predict(numeric_data)
# print(accuracy(library_predictions, wine_dataset["high_quality"]))

random.seed(123)
n_rows = wine_dataset.shape[0]
selection = random.sample(range(n_rows), 10)
print(selection)