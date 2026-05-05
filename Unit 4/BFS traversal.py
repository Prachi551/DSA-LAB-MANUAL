from collections import deque

# Graph using adjacency list
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # BFS Traversal
    def bfs(self, start):
        visited = set()
        queue = deque()

        visited.add(start)
        queue.append(start)

        print("BFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Main
g = Graph()

n = int(input("Enter number of edges: "))
print("Enter edges (u v):")

for _ in range(n):
    u, v = input().split()
    g.add_edge(u, v)

start = input("Enter start node: ")

g.bfs(start) 