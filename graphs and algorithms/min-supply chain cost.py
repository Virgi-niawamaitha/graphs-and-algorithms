def min_supply_chain_cost(cost_matrix):
    """
    Computes the minimum supply chain cost using dynamic programming.
    
    Args:
    cost_matrix (list of list): A 2D list where cost_matrix[i][j] represents the cost
                                of supplying warehouse j from supplier i.
                                
    Returns:
    int: The minimum supply chain cost.
    """
    n_suppliers = len(cost_matrix)
    n_warehouses = len(cost_matrix[0])

    # Initialize DP table
    dp = [float('inf')] * n_warehouses

    # Base case: Cost to supply the first warehouse
    dp[0] = min(cost_matrix[i][0] for i in range(n_suppliers))

    # Fill DP table for other warehouses
    for j in range(1, n_warehouses):
        dp[j] = min(dp[j - 1] + cost_matrix[i][j] for i in range(n_suppliers))

    return dp[-1]

# Example usage
cost_matrix = [
    [4, 8, 7],  # Costs from supplier 1
    [6, 5, 9],  # Costs from supplier 2
    [3, 7, 10]  # Costs from supplier 3
]
print("Minimum supply chain cost:", min_supply_chain_cost(cost_matrix))
