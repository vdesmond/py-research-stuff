#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from itertools import combinations
import numpy as np

# G = nx.karate_club_graph()
# nx.draw(G, with_labels=True, node_color="lightblue", edge_color="grey")
# plt.show()

# ERDOS RENYI
def erdos_renyi_generator(N, p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    allnodelist = list(combinations(G.nodes, 2))
    for nodepair in allnodelist:
        if bernoulli.rvs(p=p):
            G.add_edge(*nodepair)
    # nx.draw(G, with_labels=True, node_color="lightblue", edge_color="grey")
    # plt.show()
    return G


# Degree distribution
def plot_degree_distribution(G, lbl):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step", label=lbl)
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")


# G1 = erdos_renyi_generator(N=500, p=0.03)
# plot_degree_distribution(G1, 0.03)
# G2 = erdos_renyi_generator(N=500, p=0.3)
# plot_degree_distribution(G2, 0.3)
# plt.legend()
# plt.show()

# DIFFUSION OF MICROFINANCE
adj1 = np.loadtxt("village1.csv", delimiter=",")
adj2 = np.loadtxt("village2.csv", delimiter=",")

G1 = nx.to_networkx_graph(adj1)
G2 = nx.to_networkx_graph(adj2)


def graph_stats(G):
    print("No of nodes: %d" % G.number_of_nodes())
    print("No of edges: %d" % G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))


# graph_stats(G1)
# graph_stats(G2)

# plot_degree_distribution(G1, lbl="Village 1")
# plot_degree_distribution(G2, lbl="Village 2")
# plt.legend()
# plt.show()

G1_LCC = max((G1.subgraph(c) for c in nx.connected_components(G1)), key=len)
G2_LCC = max((G2.subgraph(c) for c in nx.connected_components(G2)), key=len)

print(G1_LCC.number_of_nodes() / G1.number_of_nodes())
print(G2_LCC.number_of_nodes() / G2.number_of_nodes())

# nx.draw(G2, node_size=20, node_color="blue", edge_color="grey")
# plt.show()
