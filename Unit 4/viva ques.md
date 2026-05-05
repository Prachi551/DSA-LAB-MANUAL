Experiment - 1
1. Why does inorder traversal give a sorted output?

In a Binary Search Tree (BST), the left subtree contains values smaller than the root, and the right subtree contains values greater than the root.
Inorder traversal visits nodes in the order Left → Root → Right, which naturally produces the elements in ascending (sorted) order.

2. What is the worst-case height of a BST?

The worst-case height of a BST is O(n).
This happens when the tree becomes skewed (like a linked list), for example when elements are inserted in sorted order.

3. What is the average time complexity of BST operations?

The average time complexity for operations like search, insert, and delete in a BST is O(log n).
This occurs when the tree is balanced, allowing efficient traversal.

Experiment - 2
1. What is an inorder successor?

The inorder successor of a node in a Binary Search Tree (BST) is the next node in the inorder traversal.
It is the smallest value in the right subtree of that node.

2. Why is deletion in a BST considered tricky?

Deletion is tricky because the tree structure must be adjusted while still maintaining the BST property.
There are three different cases to handle:

Deleting a leaf node
Deleting a node with one child
Deleting a node with two children (requires replacing with inorder successor)
3. How can you verify the correctness of a BST after deletion?

The correctness can be verified by performing an inorder traversal.
If the output is still sorted, it confirms that the BST property has been maintained.

Experiment - 3
1. Why is a heap used for priority queues?

A heap is used for priority queues because it allows efficient access to the highest (or lowest) priority element.
In a heap, the root always contains the minimum (min-heap) or maximum (max-heap) element, making retrieval very fast.

2. What is the time complexity of insert and extract operations?
Insertion: O(log n)
Extraction (delete min/max): O(log n)
Peek (access top element): O(1)

These complexities arise because the heap must maintain its structure using heapify operations.

3. Where are heaps used in industry?

Heaps are widely used in:

Operating systems for CPU scheduling
Graph algorithms like Dijkstra’s shortest path
Task scheduling systems
Event-driven simulations

Experiment - 4
1. What is the difference between an adjacency list and an adjacency matrix?
Adjacency List: Stores only existing edges using lists. It is space-efficient and suitable for sparse graphs.
Adjacency Matrix: Uses a 2D array to represent edges between all pairs of vertices. It is faster for edge lookup but consumes more space, especially for large graphs.
2. What is the difference between directed and undirected graphs?
Directed Graph: Edges have a direction (e.g., A → B). The connection is one-way.
Undirected Graph: Edges have no direction (e.g., A — B). The connection is two-way.
3. What are weighted graphs used for?

Weighted graphs are used when edges carry values such as cost, distance, or time.
They are commonly used in:

Navigation systems (shortest path)
Network routing
Logistics and transportation problems

Experiment-5
1. Why is a queue used in BFS?

A queue is used in Breadth-First Search (BFS) because it follows the First-In, First-Out (FIFO) principle.
This ensures that nodes are processed in the order they are discovered, enabling level-by-level traversal of the graph.

2. What is the relationship between BFS and the shortest path?

BFS can be used to find the shortest path in an unweighted graph.
Since it explores nodes level by level, the first time a node is reached is through the shortest number of edges from the source.

3. Why is the time complexity O(V + E)?

The time complexity of BFS is O(V + E) because:

Each vertex (V) is visited once
Each edge (E) is explored once

Therefore, the total work done is proportional to the sum of vertices and edges.

Experiment-6
1. What is the difference between DFS and BFS?
DFS (Depth-First Search): Explores as far as possible along one branch before backtracking. It uses a stack (or recursion).
BFS (Breadth-First Search): Explores nodes level by level. It uses a queue.
2. What is the recursion depth issue in DFS?

DFS is often implemented using recursion, which uses the call stack.
If the graph is very deep or has many nodes in a path, it can cause a stack overflow error due to excessive recursion depth.

3. What are the use cases of DFS?

DFS is commonly used in:

Path finding
Cycle detection
Topological sorting
Connected components in a graph

Experiment - 7 
1. What is a collision in a hash table?

A collision occurs when two or more keys are mapped to the same index by the hash function.
Since multiple keys share the same position, a method is needed to handle them.

2. Why does separate chaining work?

Separate chaining works because each index of the hash table stores a list (or bucket) of elements.
When multiple keys map to the same index, they are simply stored in that list, allowing all values to be preserved without overwriting.

3. What is the load factor?

The load factor is the ratio of the number of elements (n) to the size of the hash table (m).

Load Factor= ​n/m 

It indicates how full the hash table is and affects performance.

Experiment -8 
1. Trie vs Hash Map for prefix search?

A Trie is more efficient for prefix-based operations because it stores data character by character, allowing quick traversal of prefixes.
A Hash Map is efficient for exact key lookup, but it does not support efficient prefix searching.

2. What is the space trade-off in a Trie?

A Trie generally uses more memory than other data structures because it stores each character as a separate node and maintains multiple pointers.
This extra space enables faster search and prefix operations.

3. What is the use of Trie in autocomplete?

Tries are widely used in autocomplete systems.
They allow efficient retrieval of all words that share a common prefix, making them ideal for:

Search suggestions
Keyboard prediction
Dictionary-based applications

Experiment - 9
1. Can a Bloom Filter have false negatives?

No, a Bloom Filter does not produce false negatives.
If it reports that an element is not present, then it is definitely not in the set.
However, it may produce false positives, meaning it can incorrectly report that an element is present.

2. Why is a Bloom Filter memory efficient?

A Bloom Filter is memory efficient because it uses a compact bit array instead of storing the actual elements.
It represents membership information using multiple hash functions, which significantly reduces memory usage compared to traditional data structures.

3. Where is a Bloom Filter used in industry?

Bloom Filters are used in:

Databases to check if an item may exist before performing expensive queries
Caching systems to avoid unnecessary lookups
Security systems for tasks like checking malicious URLs or filtering spam