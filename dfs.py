def dfs(graph, start, visited=None):

    # Initialize visited set on first call
    if visited is None:
        visited = set()

    # Mark current vertex as visited and print it
    visited.add(start)
    print(start, end=' -> ')

    # Visit all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Define the graph from the image
graph = {
    'u': ['v', 'x'],
    'v': ['y'],
    'w': ['y', 'z'],
    'x': ['v'],
    'y': ['x'],
    'z': ['z']
}

# Run DFS starting from vertex 'u'
print("DFS traversal starting from u:")
dfs(graph, 'u')