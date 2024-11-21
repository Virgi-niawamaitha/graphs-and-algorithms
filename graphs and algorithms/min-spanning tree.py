import networkx as nx

def compute_minimum_spanning_tree(graph):
    """
    Computes the Minimum Spanning Tree (MST) for a given graph.

    Args:
    graph (networkx.Graph): The input graph with edge weights.

    Returns:
    networkx.Graph: The Minimum Spanning Tree as a subgraph.
    """
    mst = nx.minimum_spanning_tree(graph, algorithm="kruskal")
    return mst

# Example graph (weighted undirected)
# Nodes represent cities, and edges represent connection costs
graph = nx.Graph()
graph.add_weighted_edges_from([
    ("City1", "City2", 4),
    ("City1", "City3", 2),
    ("City2", "City3", 1),
    ("City2", "City4", 7),
    ("City3", "City4", 3),
    ("City3", "City5", 5),
    ("City4", "City5", 6),
])

# Compute the MST
mst = compute_minimum_spanning_tree(graph)

# Display the MST edges and their weights
print("Edges in the Minimum Spanning Tree:")
for u, v, weight in mst.edges(data=True):
    print(f"{u} - {v}: {weight['weight']}")
