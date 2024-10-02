# Floyd-Warshall algorithm for finding the shortest path between all pairs of vertices
def floyd_warshall(graph):
    V = len(graph)
    
    # Initialize distance array
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]
    
    # Add vertices one by one
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Update the distance to include vertex k in the shortest path
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    print_solution(dist)

# Utility function to print the solution matrix
def print_solution(dist):
    V = len(dist)
    print("All-Pairs Shortest Paths:")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == float('inf'):
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()

# Example graph represented as an adjacency matrix (INF = no direct edge)
INF = float('inf')
graph = [[0, 3, INF, 7],
         [8, 0, 2, INF],
         [5, INF, 0, 1],
         [2, INF, INF, 0]]

floyd_warshall(graph)
