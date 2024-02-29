import networkx as nx
import matplotlib.pyplot as plt

# Example graph
edges = [(0, 1), (0, 2), (1, 2),(2,0), (2, 3),(3,3)]

# Create graph object
G = nx.Graph()

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=15, font_weight='bold')

# Display the graph
plt.title('Graph Visualization')
plt.show()
