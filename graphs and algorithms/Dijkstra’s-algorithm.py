import heapq

def dijkstra(graph, start):
    # Create a priority queue and distances dictionary
    pq = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue

        visited.add(current_node)
        
        # Update distances to neighbors
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))
    
    return distances

# Graph represented as an adjacency list (node: [(neighbor, weight), ...])
graph = {
    'W': [('L1', 2), ('L2', 4), ('L3', 6)],
    'L1': [('L4', 3)],
    'L2': [('L4', 1)],
    'L3': [('L5', 2)],
    'L4': [('L5', 5)],
    'L5': []
}

# Calculate shortest paths from the warehouse (W)
shortest_paths = dijkstra(graph, 'W')
print(shortest_paths)
