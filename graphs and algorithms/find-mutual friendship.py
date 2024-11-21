def find_mutual_friends(graph, user1, user2):
    """
    Finds mutual friends between two users in a social network graph.

    Args:
    graph (dict): Adjacency list representing the graph.
    user1, user2 (str): The two users whose mutual friends we want to find.

    Returns:
    list: A list of mutual friends.
    """
    # Get the neighbors (friends) of both users
    friends_user1 = set(graph.get(user1, []))
    friends_user2 = set(graph.get(user2, []))
    
    # Find mutual friends (intersection of neighbors)
    mutual_friends = friends_user1.intersection(friends_user2)
    
    return list(mutual_friends)

# Example social network graph
social_network = {
    "Alice": ["Bob", "Charlie", "David"],
    "Bob": ["Alice", "Charlie"],
    "Charlie": ["Alice", "Bob", "David"],
    "David": ["Alice", "Charlie"],
    "Eve": ["Frank"],
    "Frank": ["Eve"]
}

# Find mutual friends between Alice and Charlie
user1 = "Alice"
user2 = "Charlie"
mutual_friends = find_mutual_friends(social_network, user1, user2)
print(f"Mutual friends between {user1} and {user2}: {mutual_friends}")
