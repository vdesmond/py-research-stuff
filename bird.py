#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import cartopy.crs as ccrs
import cartopy.feature as cfeature


plt.figure(figsize=(10, 10))
birddata = pd.read_csv("bird_tracking.csv")
bird_names = pd.unique(birddata.bird_name)
# bird_names = pd.unique(birddata.bird_name)
# for bird_name in bird_names:
#     index = birddata.bird_name == bird_name
#     x, y = birddata.longitude[index], birddata.latitude[index]
#     plt.plot(x, y, ".", label=bird_name)
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.legend()
# plt.show()


speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)
# plt.hist(speed[~ind], bins=np.linspace(0, 30, 20), density=True)
# plt.xlabel("2D speed in m/s")
# plt.ylabel("Frequency of occurence (norm)")
# plt.show()

# bird_names = pd.unique(birddata.bird_name)
# speed_list = []
# for bird_name in bird_names:
#     index = birddata.bird_name == bird_name
#     speed = birddata.speed_2d[index]
#     ind = np.isnan(speed)
#     speed_list.append(speed[~ind])
# plt.hist(speed_list, bins=np.linspace(0, 30, 20), density=True, label=bird_names)
# plt.xlabel("2D speed in m/s")
# plt.ylabel("Frequency of occurence (norm)")
# plt.legend()
# plt.show()

# timestamps = []
# for i in range(len(birddata)):
#     date_str = birddata.date_time.iloc[i]
#     date_obj = datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")
#     timestamps.append(date_obj)
# birddata["timestamp"] = pd.Series(timestamps, index=birddata.index)

# for bird_name in bird_names:
#     index = birddata.bird_name == bird_name
#     times = birddata.timestamp[birddata.bird_name == bird_name]
#     elapsed_time = [time - times.iloc[0] for time in times]
#     plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1), label=bird_name)
#     # print(*elapsed_time[0:20], sep="\n")
# plt.xlabel("Observation")
# plt.ylabel("Elapsed time (days)")
# plt.legend()
# plt.show()

# DAILY MEAN SPEED
# for bird_name in bird_names:
#     index = birddata.bird_name == bird_name
#     times = birddata.timestamp[birddata.bird_name == bird_name]
#     speed = birddata.speed_2d[birddata.bird_name == bird_name]
#     elapsed_time = [time - times.iloc[0] for time in times]
#     elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)
#     next_day = 1
#     inds = []
#     daily_mean_speed = []
#     for (i, t) in enumerate(elapsed_days):
#         if t < next_day:
#             inds.append(i)
#         else:
#             daily_mean_speed.append(np.mean(speed.iloc[inds]))
#             next_day += 1
#             inds = []
#     plt.plot(daily_mean_speed, label=bird_name)
# plt.xlabel("Days")
# plt.ylabel("Mean speed (m/s")
# plt.legend()
# plt.show()

# CARTOGRAPHIC PLOT


# proj = ccrs.Mercator()

# ax = plt.axes(projection=proj)
# ax.set_extent((-25.0, 20.0, 52.0, 10.0))

# ax.add_feature(cfeature.LAND)
# ax.add_feature(cfeature.OCEAN)
# ax.add_feature(cfeature.COASTLINE)
# ax.add_feature(cfeature.BORDERS, linestyle=":")


# for name in bird_names:
#     index = birddata["bird_name"] == name
#     x, y = birddata.longitude[index], birddata.latitude[index]
#     ax.plot(x, y, ".", transform=ccrs.Geodetic(), label=name)

# plt.legend()
# plt.show()


# grouped_birds = birddata.groupby("bird_name")
# mean_speeds = grouped_birds.mean()["speed_2d"]
# mean_altitudes = grouped_birds.mean()["altitude"]
# print(mean_speeds)
# print(mean_altitudes)

birddata.date_time = pd.to_datetime(birddata.date_time, infer_datetime_format=True)
birddata["date"] = birddata["date_time"].dt.date.astype("datetime64")
# grouped_bydates = birddata.groupby("date")
# mean_altitudes_perday = grouped_bydates.mean()["altitude"]
# print(mean_altitudes_perday[25:30])

grouped_birdday = birddata.groupby(
    ["bird_name", "date"],
)
# mean_altitudes_perday = grouped_birdday.mean()["altitude"]
# print(mean_altitudes_perday.loc["2013-08-18"])
eric_daily_speed = grouped_birdday.speed_2d.mean()["Eric"]
sanne_daily_speed = grouped_birdday.speed_2d.mean()["Sanne"]
nico_daily_speed = grouped_birdday.speed_2d.mean()["Nico"]

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend()
# plt.show()

print(nico_daily_speed[200:])