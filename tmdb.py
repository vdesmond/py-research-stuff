#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# df = pd.read_csv("tmdbs.csv", index_col=0)
# df["profitable"] = (df.revenue > df.budget) * 1
# regression_target = "revenue"
# classification_target = "profitable"
# df.replace([np.inf, -np.inf], np.nan, inplace=True)
# df.dropna(inplace=True)

# list_genres = df.genres.apply(lambda x: x.split(","))
# all_genres = []
# for row in list_genres:
#     genres = [x.strip() for x in row]
#     for genre in genres:
#         all_genres.append(genre)
# unique_genres = set(all_genres)
# for genre in unique_genres:
#     df[genre] = df["genres"].str.contains(genre).astype(int)

# continuous_covariates = [
#     "budget",
#     "popularity",
#     "runtime",
#     "vote_count",
#     "vote_average",
# ]

# outcomes_and_continuous_covariates = continuous_covariates + [
#     regression_target,
#     classification_target,
# ]

# plotting_variables = ["budget", "popularity", regression_target]

# axes = pd.plotting.scatter_matrix(
#     df[plotting_variables],
#     alpha=0.15,
#     color=(0, 0, 0),
#     hist_kwds={"color": (0, 0, 0)},
#     facecolor=(1, 0, 0),
# )
# # plt.show()
# # print(df[outcomes_and_continuous_covariates].skew())
# skew_data = df[outcomes_and_continuous_covariates].skew()
# right_skewed_variables = list(skew_data[skew_data > 0].index.values)
# df[right_skewed_variables] = df[right_skewed_variables].transform(
#     lambda x: np.log(x + 1)
# )
# # print(df[outcomes_and_continuous_covariates].skew())
# # df.to_csv("tmdb_clean.csv")

df = pd.read_csv("tmdb_clean.csv", index_col=0)

regression_target = "revenue"
classification_target = "profitable"
all_covariates = [
    "budget",
    "popularity",
    "runtime",
    "vote_count",
    "vote_average",
    "Action",
    "Adventure",
    "Fantasy",
    "Science Fiction",
    "Crime",
    "Drama",
    "Thriller",
    "Animation",
    "Family",
    "Western",
    "Comedy",
    "Romance",
    "Horror",
    "Mystery",
    "War",
    "History",
    "Music",
    "Documentary",
    "TV Movie",
    "Foreign",
]

# regression_outcome = df[regression_target]
# classification_outcome = df[classification_target]
# covariates = df[all_covariates]

# linear_regression = LinearRegression()
# logistic_regression = LogisticRegression()
# forest_regression = RandomForestRegressor(max_depth=4, random_state=0)
# forest_classifier = RandomForestClassifier(max_depth=4, random_state=0)


def correlation(estimator, X, y):
    predictions = estimator.fit(X, y).predict(X)
    return r2_score(predictions, y)


def accuracy(estimator, X, y):
    predictions = estimator.fit(X, y).predict(X)
    return accuracy_score(predictions, y)


# linear_regression_scores = cross_val_score(
#     linear_regression, covariates, regression_outcome, cv=10, scoring=correlation
# )
# forest_regression_scores = cross_val_score(
#     forest_regression, covariates, regression_outcome, cv=10, scoring=correlation
# )

# plt.axes().set_aspect("equal", "box")
# plt.scatter(linear_regression_scores, forest_regression_scores)
# plt.plot((0, 1), (0, 1), "k-")
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.xlabel("Linear Regression Score")
# plt.ylabel("Forest Regression Score")

# plt.show()

# logistic_regression_scores = cross_val_score(
#     logistic_regression, covariates, classification_outcome, cv=10, scoring=accuracy
# )

# forest_classification_scores = cross_val_score(
#     forest_classifier, covariates, classification_outcome, cv=10, scoring=accuracy
# )

# plt.axes().set_aspect("equal", "box")
# plt.scatter(logistic_regression_scores, forest_classification_scores)
# plt.plot((0, 1), (0, 1), "k-")

# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.xlabel("Linear Classification Score")
# plt.ylabel("Forest Classification Score")
# plt.show()

positive_revenue_df = df[df.revenue > 0]

# Replace the dataframe in the following code, and run.
regression_outcome = positive_revenue_df[regression_target]
classification_outcome = positive_revenue_df[classification_target]
covariates = positive_revenue_df[all_covariates]

# Reinstantiate all regression models and classifiers.
linear_regression = LinearRegression()
logistic_regression = LogisticRegression()
forest_regression = RandomForestRegressor(max_depth=4, random_state=0)
forest_classifier = RandomForestClassifier(max_depth=4, random_state=0)
linear_regression_scores = cross_val_score(
    linear_regression, covariates, regression_outcome, cv=10, scoring=correlation
)
forest_regression_scores = cross_val_score(
    forest_regression, covariates, regression_outcome, cv=10, scoring=correlation
)
logistic_regression_scores = cross_val_score(
    logistic_regression, covariates, classification_outcome, cv=10, scoring=accuracy
)
forest_classification_scores = cross_val_score(
    forest_classifier, covariates, classification_outcome, cv=10, scoring=accuracy
)


# plt.axes().set_aspect("equal", "box")
print(logistic_regression_scores, forest_classification_scores)
plt.scatter(logistic_regression_scores, forest_classification_scores)
plt.plot((0, 1), (0, 1), "k-")

# plt.xlim(0, 1)
# plt.ylim(0, 1)
plt.xlabel("Linear Classification Score")
plt.ylabel("Forest Classification Score")

plt.show()

forest_classifier.fit(positive_revenue_df[all_covariates], classification_outcome)
print(
    sorted(
        list(zip(all_covariates, forest_classifier.feature_importances_)),
        key=lambda tup: tup[1],
    )
)
