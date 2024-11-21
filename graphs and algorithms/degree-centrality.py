import networkx as nx

def calculate_degree_centrality(graph):
    """
    Calculate degree centrality for each node in the graph.

    Args:
    graph (networkx.Graph): Traffic network graph.

    Returns:
    dict: Degree centrality values for all nodes.
    """
    return nx.degree_centrality(graph)

# Example traffic network graph
traffic_network = nx.DiGraph()
# Add nodes (intersections) and edges (roads with direction)
traffic_network.add_edges_from([
    ("A", "B"), ("A", "C"), ("B", "C"), ("C", "D"),
    ("D", "A"), ("D", "E"), ("E", "F"), ("F", "A"),
])

# Calculate degree centrality
degree_centrality = calculate_degree_centrality(traffic_network)

# Display the degree centrality
print("Degree Centrality of Intersections:")
for intersection, centrality in degree_centrality.items():
    print(f"{intersection}: {centrality:.2f}")
