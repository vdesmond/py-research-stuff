#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

pd.options.mode.chained_assignment = None

train_time_series = pd.read_csv("train_time_series.csv", index_col=0)
train_labels = pd.read_csv("train_labels.csv", index_col=0)

new_index = list(range(train_labels.index[0], train_labels.index[-1], 1))
train_labels = train_labels.reindex(new_index)

train_time_series[["std_x", "std_y", "std_z"]] = (
    train_time_series[["x", "y", "z"]].rolling(100).std()
)
train_time_series[["mean_x", "mean_y", "mean_z"]] = (
    train_time_series[["x", "y", "z"]].rolling(100).mean()
)
train_time_series.fillna(method="ffill", inplace=True)
train_time_series.fillna(method="bfill", inplace=True)

X = train_time_series[
    ["x", "y", "z", "std_x", "std_y", "std_z", "mean_x", "mean_y", "mean_z"]
][3:][:-1]
y = train_labels["label"]
y.fillna(method="ffill", inplace=True)

# print(y.value_counts())

X_train, X_validation, y_train, y_validation = train_test_split(
    X, y, test_size=0.2, random_state=0
)

forest_classifier = RandomForestClassifier(n_estimators=300, criterion="entropy")
forest_classifier.fit(X_train, y_train)
print(forest_classifier.score(X_validation, y_validation))


# predict = forest_classifier.predict(X_test)