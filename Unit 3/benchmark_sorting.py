import time
import random

# ---------------- Sorting Algorithms ---------------- #

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


# ---------------- Dataset Generation ---------------- #

def generate_datasets(size, seed):
    random.seed(seed)

    random_data = [random.randint(1, 10000) for _ in range(size)]
    sorted_data = sorted(random_data)
    reverse_data = sorted_data[::-1]

    return random_data, sorted_data, reverse_data


# ---------------- Timing Function ---------------- #

def measure_time(func, arr):
    start = time.time()
    func(arr.copy())   # copy important ✔️
    end = time.time()
    return round(end - start, 6)


# ---------------- Main ---------------- #

sizes = [1000, 5000, 10000]
seed = int(input("Enter seed: "))

print("\n--- Timing Table (seconds) ---\n")

for size in sizes:
    print(f"\nSize: {size}")

    random_data, sorted_data, reverse_data = generate_datasets(size, seed)

    print("Type\t\tInsertion\tMerge\t\tQuick")

    for name, data in [("Random", random_data),
                       ("Sorted", sorted_data),
                       ("Reverse", reverse_data)]:

        t1 = measure_time(insertion_sort, data)
        t2 = measure_time(merge_sort, data)
        t3 = measure_time(quick_sort, data)

        print(f"{name}\t\t{t1}\t\t{t2}\t\t{t3}") 