class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        """Find the root of the set that item belongs to."""
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, x, y):
        """Union of two sets."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

def kruskal_mst(edges, vertices):

    # Sort edges by weight
    sorted_edges = sorted(edges)

    # Initialize Union-Find data structure
    uf = UnionFind(vertices)

    mst_edges = []
    total_weight = 0

    # Process edges in ascending order of weight
    for weight, v1, v2 in sorted_edges:
        # If vertices are not in the same set, add edge to MST
        if uf.find(v1) != uf.find(v2):
            uf.union(v1, v2)
            mst_edges.append((v1, v2, weight))
            total_weight += weight

    return mst_edges, total_weight

# Define the graph from the image
vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
edges = [
    (1, 'h', 'g'),  # weight, vertex1, vertex2
    (2, 'g', 'f'),
    (2, 'i', 'c'),
    (4, 'a', 'b'),
    (4, 'c', 'f'),
    (6, 'i', 'g'),
    (7, 'c', 'd'),
    (7, 'b', 'i'),
    (8, 'a', 'h'),
    (8, 'b', 'c'),
    (9, 'd', 'e'),
    (10, 'e', 'f'),
    (11, 'b', 'h'),
    (14, 'd', 'f')
]

# Run Kruskal's algorithm
mst_edges, total_weight = kruskal_mst(edges, vertices)

print("Edges in the Minimum Spanning Tree:")
for v1, v2, weight in mst_edges:
    print(f"{v1} -- {weight} -- {v2}")
print(f"\nTotal MST weight: {total_weight}")