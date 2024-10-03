# Import necessary libraries
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty undirected weighted graph
G = nx.Graph()

# Add nodes to the graph
nodes_list = [1, 2, 3, 4, 5, 6, 7]
G.add_nodes_from(nodes_list)

# Add weighted edges to the graph
edges_list = [
    (1, 2, 13), (1, 4, 4), (2, 3, 2), (2, 4, 6), (2, 5, 4),
    (3, 5, 5), (3, 6, 6), (4, 5, 3), (4, 7, 4), (5, 6, 8),
    (5, 7, 7), (6, 7, 3)
]
G.add_weighted_edges_from(edges_list)

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Define the layout for node positions
weight_labels = nx.get_edge_attributes(G, 'weight')

# Draw nodes and edges
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_color='black', font_weight='bold', edge_color='gray', width=2)

# Draw edge labels (weights)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weight_labels)

# Show the plot
plt.title("Graph with Weighted Edges")
plt.show()

# Find the shortest paths from node 1 using edge weights
shortest_paths_from_1 = nx.shortest_path(G, source=1, weight="weight")

# Find the shortest path from node 1 to node 6
shortest_path_1_to_6 = nx.shortest_path(G, source=1, target=6, weight="weight")

# Find the length of the shortest path from node 1 to node 6
shortest_path_length_1_to_6 = nx.shortest_path_length(G, source=1, target=6, weight="weight")

# Print the results
print("All shortest paths from node 1: ", shortest_paths_from_1)
print("Shortest path from node 1 to node 6: ", shortest_path_1_to_6)
print("Length of the shortest path from node 1 to node 6: ", shortest_path_length_1_to_6)
