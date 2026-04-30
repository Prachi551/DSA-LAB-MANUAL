def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # swap if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # move max to end
        heapify(arr, i, 0)

    return arr


# Input
arr = list(map(int, input("Enter elements: ").split()))

# Function call
sorted_arr = heap_sort(arr)

# Output
print("Sorted Array:", sorted_arr)