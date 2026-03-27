Experiment 1
1. Why is index access O(1)?
Array elements are stored in continuous memory locations.So, no searching is required—memory location is accessed instantly.Hence, index access takes constant time → O(1)
2.  Why is insertion at start O(n)?
When inserting at the beginning, All existing elements must shift one position to the right.Before: [10, 20, 30]
After inserting 5 → [5, 10, 20, 30].
Steps:
Shift 30
Shift 20
Shift 10
Insert 5
Number of shifts ≈ number of elements (n)
Therefore, time complexity is O(n)
3. Static vs dynamic arrays?
| Feature     | Static Array     | Dynamic Array                   |
| ----------- | ---------------- | ------------------------------- |
| Size        | Fixed            | Resizable                       |
| Memory      | Allocated once   | Reallocated when needed         |
| Flexibility | Low              | High                            |
| Speed       | Faster           | Slight overhead due to resizing |
| Example     | `int arr[5]` (C) | Python list, Java ArrayList     |
Static Array: size cannot change after creation
Dynamic Array: size can grow/shrink; may require copying elements during resize


Experiment-2
1. Complexity of scanning a matrix?
If a matrix has n rows and m columns, total elements = n × m
To scan (visit every element), we use nested loops:
Outer loop → rows (n)
Inner loop → columns (m)
Total operations = n × m
Time Complexity = O(n × m)

2. Real-world use of 2D arrays?

2D arrays represent tabular data (rows × columns).
Common uses:
Marksheet / student records (rows = students, columns = subjects)
Images (pixels stored in rows & columns)
Excel sheets / tables
Game boards (chess, tic-tac-toe)
Matrices in maths & AI
So, anywhere data is in table form → 2D arrays used

3. Memory layout idea (row-wise)?
In most languages (like C, C++, Python internally), 2D arrays are stored in row-major order
 Meaning:
First, all elements of row 1 stored
Then all elements of row 2, and so on
Matrix:
1 2 3
4 5 6
Stored in memory as:
1 2 3 4 5 6
This helps in fast access and traversal.

Experiment -3
1. What is amortized complexity?
Amortized complexity means average time per operation over many operations.
In dynamic arrays:
Most append() operations take O(1)
Sometimes resizing takes O(n)
But resizing doesn’t happen every time
So overall average per operation = Amortized O(1)

2. Why doubling helps?
When array is full, size is doubled (e.g., 4 → 8 → 16)
This reduces how often resizing happens
If we increase size by +1 → resizing happens frequently 
If we double → resizing happens rarely 
Fewer resizes = better performance
Hence, doubling ensures amortized O(1) append

3. Why pop-end is O(1)?
Removing last element does NOT require shifting
Example:
[10, 20, 30] → pop → [10, 20]
Just decrease size / remove last element
No traversal or shifting → O(1)

Experiment -4
1. Why search is O(n)?
Linked list elements are not stored contiguously
To find an element:
Start from head
Traverse node by node
In worst case, visit all nodes
Time complexity = O(n)

2. Why insert-at-head is O(1)?
Steps:
Create new node
Point it to current head
Update head
new.next = head
head = new
No traversal needed
Hence, constant time → O(1)

3. Node structure?
Each node in singly linked list has:
Node:
| data | next |
data → stores value
next → stores address of next node
Last node points to NULL

Experiment -5
1. DLL advantage over SLL?
In DLL, each node has prev + next pointers
Advantages:
Can traverse both forward & backward
Easier deletion (no need to track previous node)
Better for operations like undo/redo
Hence, DLL is more flexible than SLL

2. Browser history mapping?
Browser history works like a Doubly Linked List
Each page:
Points to previous page (back)
Points to next page (forward)
Example:
Page1 ⇄ Page2 ⇄ Page3
Back button → move to prev
Forward button → move to next
So DLL is ideal for browser navigation

3. Deletion ease in DLL?
In DLL, we already have prev pointer
To delete a node:
node.prev.next = node.next
node.next.prev = node.prev
No need to traverse to find previous node
Hence, deletion is easier & faster than SLL

Experiment - 6
1. Why stack is ideal here?

👉 Stack follows LIFO (Last In First Out)
In parentheses checking:
Last opened bracket must be closed first
Example:

( [ ] ) ✔
Stack perfectly matches this behavior
Hence, stack is ideal for bracket validation

2. What fails in "([)]"?
Sequence: "([)]"
Process:
Push (
Push [
Encounter ) → should match ( but top is [ ❌
Order is incorrect (mismatch)
Hence, string is invalid

3. Underflow meaning?
Underflow = trying to pop from empty stack
Example:
Stack = empty
pop() → error
No elements available to remove
This condition is called stack underflow

Experiment -7
1. BFS uses queue?
Yes, BFS (Breadth First Search) uses a Queue
Reason:
BFS visits nodes level by level
Queue follows FIFO, so nodes are processed in the same order they are discovered
Example flow:
Start → enqueue node  
Visit → dequeue → enqueue its neighbors  
Hence, BFS uses Queue data structure

2. FIFO meaning?
FIFO = First In First Out
The element inserted first is removed first
Example:
Queue: [10, 20, 30]
Remove → 10
Just like a real-life line (queue)

3. Scheduling example?
Scheduling is based on Queue (FIFO)
Example: CPU Scheduling
Processes: P1, P2, P3
Execution: P1 → P2 → P3
First process gets executed first


