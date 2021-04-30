#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter
import numpy as np
import pandas as pd


def marginal_prob(chars):
    _keys = chars.values()
    freq = dict(Counter(_keys))
    sum_freq = sum(freq.values())
    return {char: f / sum_freq for char, f in freq.items()}


def chance_homophily(chars):
    marginal = marginal_prob(chars)
    return np.sum(np.square(list(marginal.values())))


# favorite_colors = {"ankit": "red", "xiaoyu": "blue", "mary": "blue"}

# color_homophily = chance_homophily(favorite_colors)
# print(color_homophily)

df = pd.read_csv("villagefull.csv", low_memory=False, index_col=0)
df1 = df[df["village"] == 1]
df2 = df[df["village"] == 2]

sex1 = dict(zip(df1.pid, df1.resp_gend))
caste1 = dict(zip(df1.pid, df1.caste))
religion1 = dict(zip(df1.pid, df1.religion))

sex2 = dict(zip(df2.pid, df2.resp_gend))
caste2 = dict(zip(df2.pid, df2.caste))
religion2 = dict(zip(df2.pid, df2.religion))

homophily_list = map(
    chance_homophily, [sex1, caste1, religion1, sex2, caste2, religion2]
)


def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                num_ties += 1
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    num_same_ties += 1
    return num_same_ties / num_ties


pid1 = pd.read_csv("keyvil1.csv", low_memory=False, dtype=int)["0"].to_dict()
pid2 = pd.read_csv("keyvil2.csv", low_memory=False, dtype=int)["0"].to_dict()

import networkx as nx

A1 = np.array(
    pd.read_csv(
        "adjvil1.csv",
        index_col=0,
    )
)
A2 = np.array(
    pd.read_csv(
        "adjvil2.csv",
        index_col=0,
    )
)
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

homophily_list_from_graph = map(
    homophily,
    [G1, G1, G1, G2, G2, G2],
    [sex1, caste1, religion1, sex2, caste2, religion2],
    [pid1, pid1, pid1, pid2, pid2, pid2],
)
# print(list(homophily_list))
# print(list(homophily_list_from_graph))
