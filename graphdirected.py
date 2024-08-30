import networkx as nx
import matplotlib.pyplot as plt

# Check the version of NetworkX
print(nx.__version__)

# Create a directed graph
DG = nx.DiGraph()

# Add nodes and edges as before...
DG.add_nodes_from([1, 2, 3, 4])
DG.add_edge(1, 2)
DG.add_edge(2, 3)
DG.add_edge(3, 4)
DG.add_edge(4, 1)

# Draw the directed graph
nx.draw(DG, with_labels=True, node_color='lightblue', arrowsize=20)
plt.title("Directed Graph")
plt.show()
