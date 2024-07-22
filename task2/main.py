from dfs import dfs
from bfs import bfs

import networkx as nx
import matplotlib.pyplot as plt

def get_graph():
    G = nx.DiGraph()

    # Adding nodes (stations or stops)
    nodes = ["Station A", "Station B", "Station C", "Station D", "Station E"]
    G.add_nodes_from(nodes)

    # Adding edges (routes between stations)
    edges = [("Station A", "Station B"), ("Station B", "Station C"), ("Station C", "Station D"),
            ("Station D", "Station E"), ("Station E", "Station A"), ("Station B", "Station D")]
    G.add_edges_from(edges)
    return G

def main():
    G = get_graph()
    dfs_result = list(dfs(G, "Station A", "Station E"))
    bfs_result = list(bfs(G, "Station A", "Station E"))
    print(dfs_result)
    print(bfs_result)

if __name__ == "__main__":
    main()