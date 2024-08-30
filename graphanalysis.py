import networkx as nx

# Create a graph with two components
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (4, 5)])

# Find all connected components
connected_components = list(nx.connected_components(G))

print("Connected components:", connected_components)
