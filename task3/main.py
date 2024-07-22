import networkx as nx
import matplotlib.pyplot as plt
import heapq


def get_graph():
    G = nx.DiGraph()

    nodes = ["Station A", "Station B", "Station C", "Station D", "Station E"]
    G.add_nodes_from(nodes)

    G = nx.DiGraph()
    nodes = ["Station A", "Station B", "Station C", "Station D", "Station E"]
    edges = [("Station A", "Station B", 3), ("Station B", "Station C", 5), ("Station C", "Station D", 2),
            ("Station D", "Station E", 1), ("Station E", "Station A", 4), ("Station B", "Station D", 1)]
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    return G

def dijkstra(graph, source):
    inf = float('inf')
    distances = {node: inf for node in graph.nodes()}
    distances[source] = 0
    path = {node: [] for node in graph.nodes()}
    path[source] = [source]
    priority_queue = [(0, source)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Перевірка на кожного сусіда поточного вузла
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            
            # Перевірка чи знайдено кращий шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = path[current_node] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, path

def main():
    source = 'Station A'
    distances, paths = dijkstra(get_graph(), source)
    print("Distances from Station A:", distances)
    print("Paths from Station A:", paths)

if __name__ == "__main__":
    main()