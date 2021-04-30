#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

whisky = pd.read_csv("whiskies.csv")
whisky["Regions"] = pd.read_csv("regions.csv")
# print(whisky.head())
# print(whisky.columns)
flavors = whisky.iloc[:, 2:14]
# print(flavors)
corr_flavors = pd.DataFrame.corr(flavors)
# print(corr_flavors)

import matplotlib.pyplot as plt

corr_whiskey = pd.DataFrame.corr(flavors.transpose())
# plt.figure(figsize=(10, 10))
# plt.matshow(corr_whiskey, cmap="RdBu")
# plt.colorbar()
# plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2)
a1 = ax1.pcolor(corr_whiskey, cmap="RdBu")

import seaborn as sns

# heatmap = sns.heatmap(
#     corr_flavors,
#     xticklabels=corr_flavors.columns.values,
#     yticklabels=corr_flavors.columns.values,
# )
# plt.show()

# heatmap = sns.heatmap(
#     corr_whiskey,
#     ax=ax1
#     # xticklabels=corr_whiskey.columns.values,
#     # yticklabels=corr_whiskey.columns.values,
# )

from sklearn.cluster.bicluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whiskey)
# print(np.sum(model.rows_, axis=1))

whisky["Group"] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.iloc[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)
flavors_ = whisky.iloc[:, 2:14]
correlations = pd.DataFrame.corr(flavors_.transpose())
correlations = np.array(correlations)


a2 = ax2.pcolor(correlations, cmap="RdBu")
plt.colorbar(a1, ax=ax1)
plt.colorbar(a2, ax=ax2)
plt.show()