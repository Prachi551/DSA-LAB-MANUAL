from collections import deque

# ---------------- PROFILES ----------------
class User:
    def __init__(self, name):
        self.name = name
        self.interests = []

class SocialNetwork:
    def __init__(self):
        self.users = {}   # hashing
        self.graph = {}   # adjacency list

    # Add user
    def add_user(self, name):
        self.users[name] = User(name)
        self.graph[name] = []

    def update_profile(self, name, interests):
        self.users[name].interests = interests

    def get_profile(self, name):
        return self.users[name].interests

    # ---------------- GRAPH ----------------
    def add_friend(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_friend(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def get_friends(self, u):
        return self.graph[u]

    # ---------------- BFS (Shortest Path) ----------------
    def bfs_shortest_path(self, start, end):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            node, path = queue.popleft()

            if node == end:
                return path

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None

    # ---------------- DFS (Depth Search) ----------------
    def dfs(self, node, visited, depth):
        if depth < 0:
            return
        visited.add(node)
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, depth - 1)

    # ---------------- RECOMMENDATION ----------------
    def suggest(self, user):
        suggestions = {}
        user_interests = set(self.users[user].interests)

        for other in self.users:
            if other != user:
                common = len(user_interests & set(self.users[other].interests))
                if common > 0:
                    suggestions[other] = common

        # sort by common interests
        return sorted(suggestions.items(), key=lambda x: x[1], reverse=True)


# ---------------- MAIN DEMO ----------------
sn = SocialNetwork()

# Add users
for u in ["A", "B", "C", "D", "E", "F"]:
    sn.add_user(u)

# Update profiles
sn.update_profile("A", ["music", "sports"])
sn.update_profile("B", ["music", "movies"])
sn.update_profile("C", ["sports", "travel"])
sn.update_profile("D", ["movies", "travel"])
sn.update_profile("E", ["music", "travel"])
sn.update_profile("F", ["sports"])

# Add connections
connections = [("A","B"), ("A","C"), ("B","D"), ("C","E"), ("D","F"), ("E","F")]
for u, v in connections:
    sn.add_friend(u, v)

print("\n--- Profiles ---")
for u in sn.users:
    print(u, ":", sn.get_profile(u))

# BFS shortest path
print("\n--- BFS Shortest Path ---")
print("A to F:", sn.bfs_shortest_path("A", "F"))

# DFS exploration
print("\n--- DFS (depth=2 from A) ---")
sn.dfs("A", set(), 2)

# Recommendation
print("\n\n--- Suggestions for A ---")
print(sn.suggest("A"))

# Remove connection
sn.remove_friend("A", "B")
print("\nAfter removing A-B:", sn.get_friends("A"))