#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pd.options.mode.chained_assignment = None
train_time_series = pd.read_csv("train_time_series.csv", index_col=0)
train_labels = pd.read_csv("train_labels.csv", index_col=0)

# train_time_series.timestamp -= train_time_series.timestamp.iloc[0]
new_index = list(range(train_labels.index[0], train_labels.index[-1], 1))
train_labels = train_labels.reindex(new_index)

train_df = train_time_series[3:]
train_df.drop(["UTC time", "timestamp", "accuracy"], axis=1, inplace=True)
train_df["label"] = train_labels["label"]
train_df.reset_index(inplace=True)
train_df.fillna(method="ffill", inplace=True)

# Plotting accelorometer data

colors = {1: "r", 2: "b", 3: "c", 4: "g"}
train_df["color"] = train_df["label"].apply(lambda label: colors[label])
fig, ax = plt.subplots()

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()


def gen_repeating(df):
    i = 0
    while i < len(df):
        j = i
        while j < len(df) and df[j] == df[i]:
            j += 1
        yield (df[i], i, j - 1)
        i = j


for color, start, end in gen_repeating(train_df["color"]):
    if start > 0:
        start -= 1
    idx = train_df.index[start : end + 1]
    train_df.loc[idx, "z"].plot(ax=ax, color=color, label="")

## Get artists and labels for legend and chose which ones to display
handles, labels = ax.get_legend_handles_labels()

## Create custom artists
r_line = plt.Line2D((0, 1), (0, 0), color="r")
b_line = plt.Line2D((0, 1), (0, 0), color="b")
c_line = plt.Line2D((0, 1), (0, 0), color="c")
g_line = plt.Line2D((0, 1), (0, 0), color="g")

## Create legend from custom artist/label lists
ax.legend(
    handles + [r_line, c_line, b_line, g_line],
    labels
    + [
        "Standing",
        "Walking",
        "Stairs Up",
        "Stairs Down",
    ],
    loc="upper right",
)

# Display plot
plt.title("Accelerometer Z data")
fig.set_size_inches(20, 11)
plt.savefig("Z2.png", bbox_inches="tight")
