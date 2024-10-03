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


import sys
import numpy as np

# Function to calculate the lower bound for a given node
def calculate_lower_bound(adj_matrix, path, level, n):
    bound = 0
    # Add the edge weights for the current path
    for i in range(1, level):
        bound += adj_matrix[path[i - 1]][path[i]]
    # Add minimum cost for unvisited cities
    for i in range(n):
        if i not in path:
            bound += min([adj_matrix[i][j] for j in range(n) if j not in path and i != j])
    return bound

# Function to solve TSP using Branch and Bound
def tsp_branch_and_bound(adj_matrix, n):
    # Initial path starting from the first city
    path = [0] * (n + 1)
    path[0] = 0
    visited = [False] * n
    visited[0] = True
    final_path = [None] * (n + 1)
    min_cost = sys.maxsize

    def solve(current_bound, current_weight, level, current_path):
        nonlocal min_cost, final_path

        # If all cities are visited, check if we have a better solution
        if level == n:
            if adj_matrix[current_path[level - 1]][current_path[0]] != 0:
                total_cost = current_weight + adj_matrix[current_path[level - 1]][current_path[0]]
                if total_cost < min_cost:
                    final_path[:n + 1] = current_path[:]
                    final_path[n] = current_path[0]
                    min_cost = total_cost
            return

        # Try all cities not visited yet
        for i in range(n):
            if adj_matrix[current_path[level - 1]][i] != 0 and not visited[i]:
                temp = current_bound
                current_weight += adj_matrix[current_path[level - 1]][i]
                current_bound = calculate_lower_bound(adj_matrix, current_path[:level + 1], level + 1, n)
                if current_bound + current_weight < min_cost:
                    current_path[level] = i
                    visited[i] = True
                    solve(current_bound, current_weight, level + 1, current_path)
                current_weight -= adj_matrix[current_path[level - 1]][i]
                current_bound = temp
                visited[i] = False

    current_bound = 0
    current_weight = 0
    solve(current_bound, current_weight, 1, path)
    return final_path, min_cost

# Main function to run the TSP solution
if __name__ == "__main__":
    # Example graph (adjacency matrix)
    adj_matrix = [[0, 29, 20, 21],
                  [29, 0, 15, 17],
                  [20, 15, 0, 28],
                  [21, 17, 28, 0]]
    
    n = len(adj_matrix)
    optimal_path, min_cost = tsp_branch_and_bound(adj_matrix, n)

    print("Optimal Path: ", optimal_path)
    print("Minimum Cost: ", min_cost)

