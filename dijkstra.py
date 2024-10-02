import sys

# Function to find the vertex with the minimum distance that hasn't been visited
def min_distance(dist, visited, V):
    min_val = sys.maxsize
    min_index = -1
    
    for v in range(V):
        if dist[v] < min_val and not visited[v]:
            min_val = dist[v]
            min_index = v
    
    return min_index

# Dijkstra's algorithm to find the shortest path from source to all other vertices
def dijkstra(graph, src):
    V = len(graph)
    dist = [sys.maxsize] * V  # Distance from source to all vertices
    dist[src] = 0  # Distance from source to itself is always 0
    visited = [False] * V  # Track visited vertices
    
    for _ in range(V):
        u = min_distance(dist, visited, V)  # Select the minimum distance vertex
        visited[u] = True
        
        # Update the distance value of the adjacent vertices of the chosen vertex
        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
    
    # Print the result
    print("Vertex\tDistance from Source")
    for i in range(V):
        print(f"{i}\t\t{dist[i]}")

# Example graph represented as an adjacency matrix
graph = [[0, 10, 0, 0, 0, 0],
         [10, 0, 5, 0, 0, 0],
         [0, 5, 0, 20, 1, 0],
         [0, 0, 20, 0, 2, 1],
         [0, 0, 1, 2, 0, 2],
         [0, 0, 0, 1, 2, 0]]

dijkstra(graph, 0)  # Run Dijkstra's algorithm from vertex 0
