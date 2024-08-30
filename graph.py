import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.Graph()

# Add nodes with attributes
G.add_node(1, role='start')
G.add_node(2, role='middle')
G.add_node(3, role='end')

# Add edges with attributes
G.add_edge(1, 2, weight=4.2)
G.add_edge(2, 3, weight=7.1)

# Draw the graph with custom node colors based on role
node_colors = ['green' if G.nodes[n]['role'] == 'start' else 'blue' if G.nodes[n]
               ['role'] == 'middle' else 'red' for n in G.nodes]

nx.draw(G, with_labels=True, node_color=node_colors)
plt.title("Graph with Node and Edge Attributes")
plt.show()
