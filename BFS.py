from collections import deque

# Function to perform Breadth-First Search
def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the start node
    
    while queue:
        # Dequeue a node from the queue
        vertex = queue.popleft()
        
        # If the node has not been visited, mark it as visited and process it
        if vertex not in visited:
            print(vertex, end=" ")  # Process the node (e.g., print it)
            visited.add(vertex)
            
            # Enqueue all adjacent nodes that haven't been visited
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage: defining a graph using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call the BFS function
print("Breadth-First Search starting from node A:")
bfs(graph, 'A')
