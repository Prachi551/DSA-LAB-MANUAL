class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of buckets

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        # Update if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    # Get value
    def get(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        return None

    # Delete key
    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True

        return False

    # Display table
    def display(self):
        print("Hash Table:")
        for i in range(self.size):
            print(f"{i} -> ", end="")
            for k, v in self.table[i]:
                print(f"({k}:{v})", end=" ")
            print()


# Main
size = int(input("Enter table size: "))
ht = HashTable(size)

n = int(input("Enter number of elements: "))
print("Enter key value pairs:")

for _ in range(n):
    key, value = map(int, input().split())
    ht.insert(key, value)

ht.display()

# Get
key = int(input("Enter key to search: "))
result = ht.get(key)
print("Value:", result if result is not None else "Not Found")

# Delete
key = int(input("Enter key to delete: "))
if ht.delete(key):
    print("Deleted successfully")
else:
    print("Key not found")

ht.display()