Experiment- 1
1. Stable vs Unstable
Stable sorting:
It preserves the relative order of equal elements.
Unstable sorting:
It may change the order of equal elements.
Examples:
Stable → Bubble Sort, Insertion Sort
Unstable → Quick Sort, Heap Sort

2. In-place meaning
An in-place algorithm sorts the data without using extra memory (or very little).
The sorting is done within the same array.

3. Why O(n²) is slow?
Because it uses nested loops, so:
Each element is compared multiple times
Total operations ≈ n × n
For large inputs, the time increases very fast, making it slow.

Experiment-2
1. Worst-case input?
For insertion sort, the worst-case input is a reverse sorted array.
Because every element has to be compared and shifted.
Time complexity becomes O(n²).

2. Is insertion stable?
Yes, insertion sort is stable.
It keeps the relative order of equal elements unchanged.

3. Space complexity?
O(1) (constant space)
It is an in-place algorithm and does not use extra memory.

Experiment-3 
1. Why is it stable? (Merge Sort)
Because during merging, when two elements are equal, the element from the left subarray is chosen first.
This preserves the original relative order of equal elements.

2. Why does it need extra memory?
Merge sort creates temporary arrays (left and right subarrays) during splitting and merging.
Also, a new array is used to store the merged result.
Hence, space complexity = O(n).

3. Use in external sorting
Used when data is too large to fit in memory (stored on disk).
Merge sort efficiently merges sorted chunks/files.
Therefore, it is ideal for external sorting.

Experiment-4
1. Worst-case for Quick Sort?
The worst case occurs when the pivot is always the smallest or largest element.
Example: already sorted or reverse sorted array (with last/first pivot).
Time complexity becomes O(n²).

2. Is Quick Sort stable?
No, Quick Sort is not stable.
It may change the relative order of equal elements.

3. Average time?
O(n log n)
Because the array is divided into balanced partitions on average.

Experiment-5
1. Why is Heap Sort not stable?
Because it performs swaps between non-adjacent elements.
This can change the relative order of equal elements, so it is not stable.

2. Heap vs BST for Top-K?
Heap is preferred for Top-K problems.
Heap gives O(n log k) time efficiently.
BST may need balancing, otherwise it can become slow.

3. Real use of Priority Queue?
Used in systems where highest/lowest priority element is processed first.
Examples:
CPU scheduling
Dijkstra’s shortest path algorithm
Task scheduling / job processing systems 

Experiment-6
1. Why is reverse worst for insertion sort?
In a reverse sorted array, every new element has to be shifted across all previous elements to reach its correct position.
Maximum comparisons and shifts happen
Time becomes O(n²)

2. Why can Quick Sort degrade on sorted data with a bad pivot?
If the pivot is chosen as first/last element, then for a sorted array:
One partition becomes empty, the other has n−1 elements
Partitions are highly unbalanced
Time becomes O(n²)

3. Why is Merge Sort stable but uses extra memory?
Stable: During merging, equal elements keep their original order (left element chosen first).
Extra memory: It creates temporary arrays (left, right, merged array)
Space complexity = O(n) 