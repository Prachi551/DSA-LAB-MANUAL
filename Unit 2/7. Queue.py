# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue using head (front) and tail (rear)
class Queue:
    def __init__(self):
        self.head = None   # front
        self.tail = None   # rear

    def enqueue(self, val):
        new = Node(val)
        if self.tail is None:
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        print("Enqueue:", val)

    def dequeue(self):
        if self.head is None:
            print("Queue Empty")
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        print("Dequeue:", val)
        return val

    def front(self):
        if self.head:
            return self.head.data
        return None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -------------------
# Queue Operations
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.dequeue()
print("Front:", q.front())

q.enqueue(40)

print("Final Queue:")
q.display()


# -------------------
# BFS Example (Graph Traversal)

def bfs(graph, start):
    visited = set()
    q = Queue()

    q.enqueue(start)
    visited.add(start)

    print("\nBFS Traversal:")

    while q.head:
        node = q.dequeue()
        print(node, end=" ")

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.enqueue(nei)


# Simple graph
graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}

bfs(graph, 1)