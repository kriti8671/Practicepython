import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])

# Calculate and print the degree of each node
print("Degrees of each node:", dict(G.degree()))

# Calculate and print the shortest path between two nodes
print("Shortest path between 1 and 4:",
      nx.shortest_path(G, source=1, target=4))

# Calculate and print the clustering coefficient of each node
print("Clustering coefficient of each node:", nx.clustering(G))
