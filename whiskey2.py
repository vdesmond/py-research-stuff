#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.cluster.bicluster import SpectralCoclustering
import numpy as np, pandas as pd

whisky = pd.read_csv(
    "whiskies.csv",
    index_col=0,
)
correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose())
correlations = np.array(correlations)

# BOKEH
from bokeh.models import HoverTool, ColumnDataSource

# plot_values = [1, 2, 3, 4, 5]
# plot_colors = ["#0173b2", "#de8f05"]
# from itertools import product

# grid = list(product(plot_values, plot_values))
# xs, ys = zip(*grid)
# colors = [plot_colors[i % 2] for i in range(len(grid))]
# alphas = np.linspace(0, 1, len(grid))

# source = ColumnDataSource(
#     data={
#         "x": xs,
#         "y": ys,
#         "colors": colors,
#         "alphas": alphas,
#     }
# )

from bokeh.plotting import figure, output_file, show

# output_file("Basic_Example.html", title="Basic Example")
# fig = figure(tools="hover")
# fig.rect("x", "y", 0.9, 0.9, source=source, color="colors", alpha="alphas")
# hover = fig.select(dict(type=HoverTool))
# hover.tooltips = {
#     "Value": "@x, @y",
# }
# show(fig)


# CORRELATION
cluster_colors = ["#0173b2", "#de8f05", "#029e73", "#d55e00", "#cc78bc", "#ca9161"]
regions = ["Speyside", "Highlands", "Lowlands", "Islands", "Campbelltown", "Islay"]

region_colors = dict(zip(regions, cluster_colors))

distilleries = list(whisky.Distillery)
correlation_colors = []
for i in range(len(distilleries)):
    for j in range(len(distilleries)):
        if correlations[i, j] < 0.7:
            correlation_colors.append("white")
        else:
            if whisky.Group[i] == whisky.Group[j]:  # if the groups match,
                correlation_colors.append(cluster_colors[whisky.Group[i]])
            else:
                correlation_colors.append("lightgray")

source = ColumnDataSource(
    data={
        "x": np.repeat(distilleries, len(distilleries)),
        "y": list(distilleries) * len(distilleries),
        "colors": correlation_colors,
        "correlations": list(correlations.flatten()),
    }
)

output_file("Whisky Correlations.html", title="Whisky Correlations")
fig = figure(
    title="Whisky Correlations",
    x_axis_location="above",
    x_range=list(reversed(distilleries)),
    y_range=distilleries,
    tools="hover,box_zoom,reset",
)
fig.grid.grid_line_color = None
fig.axis.axis_line_color = None
fig.axis.major_tick_line_color = None
fig.axis.major_label_text_font_size = "5pt"
fig.xaxis.major_label_orientation = np.pi / 3
fig.rect("x", "y", 0.9, 0.9, source=source, color="colors", alpha="correlations")
hover = fig.select(dict(type=HoverTool))
hover.tooltips = {
    "Whiskies": "@x, @y",
    "Correlation": "@correlations",
}
show(fig)

# LOCATIONS

# points = [(0, 0), (1, 2), (3, 1)]
# xs, ys = zip(*points)
# colors = ["#0173b2", "#de8f05", "#029e73"]

# output_file("Spatial_Example.html", title="Regional Example")
# location_source = ColumnDataSource(
#     data={
#         "x": xs,
#         "y": ys,
#         "colors": colors,
#     }
# )

# fig = figure(title="Title", x_axis_location="above", tools="hover, save")
# fig.plot_width = 300
# fig.plot_height = 380
# fig.circle("x", "y", size=10, source=location_source, color="colors", line_color=None)

# hover = fig.select(dict(type=HoverTool))
# hover.tooltips = {"Location": "(@x, @y)"}
# show(fig)


def location_plot(title, colors):
    output_file(title + ".html")
    location_source = ColumnDataSource(
        data={
            "x": whisky[" Latitude"],
            "y": whisky[" Longitude"],
            "colors": colors,
            "regions": whisky.Region,
            "distilleries": whisky.Distillery,
        }
    )

    fig = figure(title=title, x_axis_location="above", tools="hover, save")
    fig.plot_width = 400
    fig.plot_height = 500
    fig.circle(
        "x", "y", size=9, source=location_source, color="colors", line_color=None
    )
    fig.xaxis.major_label_orientation = np.pi / 3
    hover = fig.select(dict(type=HoverTool))
    hover.tooltips = {"Distillery": "@distilleries", "Location": "(@x, @y)"}
    show(fig)


# region_cols = [region_colors[i] for i in whisky.Region]
# location_plot("Whisky Locations and Regions", region_cols)

region_cols = [region_colors[i] for i in whisky.Region]
classification_cols = [cluster_colors[i] for i in list(whisky["Group"])]

location_plot("Whisky Locations and Regions", region_cols)
location_plot("Whisky Locations and Groups", classification_cols)