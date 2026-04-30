def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, comparisons, swaps


# Input
arr = list(map(int, input("Enter elements: ").split()))

# Function call
sorted_arr, comp, swp = bubble_sort(arr)

# Output
print("Sorted Array:", sorted_arr)
print("Comparisons:", comp)
print("Swaps:", swp)