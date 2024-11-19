from collections import defaultdict, deque

def topologicalSort(graph):

    # Calculate in-degree for each node
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Initialize queue with nodes that have no dependencies (in-degree = 0)
    queue = deque()
    for node in graph:
        if in_degree[node] == 0:
            queue.append(node)

    result = []

    # Process nodes
    while queue:
        current = queue.popleft()
        result.append(current)

        # Reduce in-degree of all neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result

clothing_graph = {
    'undershorts': ['pants', 'shoes'],
    'socks': ['shoes'],
    'pants': ['belt', 'shoes'],
    'shirt': ['belt', 'tie'],
    'belt': ['jacket'],
    'tie': ['jacket'],
    'shoes': ['watch'],
    'watch': [],
    'jacket': []
}

# Run topological sort
sorted_items = topologicalSort(clothing_graph)
print("One valid topological ordering:", ' → '.join(sorted_items))