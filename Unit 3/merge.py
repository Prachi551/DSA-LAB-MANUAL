def merge(left, right):
    result = []
    i = j = 0

    # merge both lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= keeps it stable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# Input
arr = list(map(int, input("Enter elements: ").split()))

# Function call
sorted_arr = merge_sort(arr)

# Output
print("Sorted Array:", sorted_arr)