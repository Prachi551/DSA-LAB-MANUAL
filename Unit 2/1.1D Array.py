# Insert operation
def insert(arr, pos, val):
    shifts = 0
    arr.append(0)  # increase size

    for i in range(len(arr)-1, pos, -1):
        arr[i] = arr[i-1]
        shifts += 1

    arr[pos] = val
    print("After Insert:", arr)
    print("Shifts:", shifts)


# Delete operation
def delete(arr, pos):
    shifts = 0

    for i in range(pos, len(arr)-1):
        arr[i] = arr[i+1]
        shifts += 1

    arr.pop()
    print("After Delete:", arr)
    print("Shifts:", shifts)


# -------------------
# Main
arr = [10, 20, 30, 40]

print("Original:", arr)

# Insert at start
insert(arr, 0, 5)

# Insert at middle
insert(arr, 2, 25)

# Insert at end
insert(arr, len(arr), 50)

# Delete from start
delete(arr, 0)

# Delete from middle
delete(arr, 2)

# Delete from end
delete(arr, len(arr)-1)