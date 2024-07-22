import networkx as nx
import matplotlib.pyplot as plt

# Creating a simple example of a transportation network as a directed graph
G = nx.DiGraph()

# Adding nodes (stations or stops)
nodes = ["Station A", "Station B", "Station C", "Station D", "Station E"]
G.add_nodes_from(nodes)

# Adding edges (routes between stations)
edges = [("Station A", "Station B"), ("Station B", "Station C"), ("Station C", "Station D"),
         ("Station D", "Station E"), ("Station E", "Station A"), ("Station B", "Station D")]
G.add_edges_from(edges)

# Visualizing the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', linewidths=1, font_size=15)
plt.title('Simple Transportation Network Graph')
plt.show()

# Calculating basic characteristics of the graph
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Degress: {G.degree()}")