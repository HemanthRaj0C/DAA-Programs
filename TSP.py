import sys

# Function to find the minimum cost of visiting all cities
def tsp(graph):
    n = len(graph)  # Number of cities
    # Create a DP table with (1 << n) and n size, initialized to infinity
    dp = [[sys.maxsize] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Starting from the first city

    # Iterate over all subsets of cities
    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):  # If u is in the subset represented by mask
                for v in range(n):
                    if mask & (1 << v) == 0:  # If v is not in the subset
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + graph[u][v])

    # Finding the minimum cost to return to the starting city
    min_cost = sys.maxsize
    for u in range(1, n):
        min_cost = min(min_cost, dp[(1 << n) - 1][u] + graph[u][0])

    return min_cost

# Example usage
# Distance matrix representing the graph (cost of traveling between cities)
graph = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

min_cost = tsp(graph)
print("Minimum cost of visiting all cities:", min_cost)
