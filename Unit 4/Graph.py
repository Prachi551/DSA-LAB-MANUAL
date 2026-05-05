# Graph using adjacency list
class Graph:
    def __init__(self):
        self.graph = {}

    # Add edge (directed + weighted)
    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        
        self.graph[u].append((v, w))

    # Print graph
    def print_graph(self):
        print("Adjacency List:")
        for node in self.graph:
            print(f"{node} -> ", end="")
            for (neighbor, weight) in self.graph[node]:
                print(f"({neighbor}, weight={weight})", end=" ")
            print()


# Main
g = Graph()

n = int(input("Enter number of edges: "))

print("Enter edges (u v weight):")
for _ in range(n):
    u, v, w = input().split()
    g.add_edge(u, v, int(w))

g.print_graph() 