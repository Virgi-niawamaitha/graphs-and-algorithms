import numpy as np

def dp_inventory_management(demands, holding_cost, ordering_cost, max_inventory):
    # Number of periods (time periods)
    T = len(demands)
    
    # Initialize DP table where dp[i][j] means the minimum cost for period i with j inventory
    dp = np.inf * np.ones((T + 1, max_inventory + 1))
    dp[0][0] = 0  # No cost at the start with 0 inventory
    
    # Fill the DP table
    for i in range(1, T + 1):
        for inventory in range(max_inventory + 1):
            for order_qty in range(max_inventory + 1):
                # Calculate the inventory at the end of period i after ordering 'order_qty'
                new_inventory = inventory + order_qty - demands[i - 1]
                
                # Ensure new_inventory is within the valid bounds (0 to max_inventory)
                if 0 <= new_inventory <= max_inventory:
                    # Compute holding and ordering costs
                    holding_cost_i = holding_cost * new_inventory
                    ordering_cost_i = ordering_cost * order_qty
                    # Update the DP table
                    dp[i][new_inventory] = min(dp[i][new_inventory], dp[i - 1][inventory] + holding_cost_i + ordering_cost_i)
    
    # The optimal reorder point is the minimum cost at the last period with any inventory level
    return np.min(dp[T])

# Example usage:
demands = [5, 7, 6, 3]  # Demands for 4 periods
holding_cost = 2  # Cost per unit of inventory held
ordering_cost = 10  # Cost per order
max_inventory = 10  # Maximum inventory level

optimal_cost = dp_inventory_management(demands, holding_cost, ordering_cost, max_inventory)
print(f"The optimal cost is: {optimal_cost}")
