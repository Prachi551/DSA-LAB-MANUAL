# Program for 2D Array Operations

# Taking input for matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")

for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter element at position ({i},{j}): "))
        row.append(val)
    matrix.append(row)

# Display matrix
print("\nMatrix:")
for row in matrix:
    print(row)

# -------------------------------
# Row Sum
print("\nRow Sums:")
for i in range(rows):
    row_sum = sum(matrix[i])
    print(f"Sum of row {i} = {row_sum}")

# -------------------------------
# Column Sum
print("\nColumn Sums:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Sum of column {j} = {col_sum}")

# -------------------------------
# Search for a value
search = int(input("\nEnter value to search: "))
found = False

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == search:
            print(f"Value found at position ({i},{j})")
            found = True

if not found:
    print("Value not found in matrix")

# -------------------------------
# Transpose of Matrix
print("\nTranspose of Matrix:")

transpose = []
for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transpose.append(new_row)

for row in transpose:
    print(row)