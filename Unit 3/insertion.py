def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # shift elements greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Input
arr = list(map(int, input("Enter elements: ").split()))

# Function call
sorted_arr = insertion_sort(arr)

# Output
print("Sorted Array:", sorted_arr)