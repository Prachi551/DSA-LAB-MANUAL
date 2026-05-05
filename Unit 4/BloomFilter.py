class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = [0] * size

    # Simple hash functions
    def hash1(self, item):
        return hash(item) % self.size

    def hash2(self, item):
        return (hash(item) * 7) % self.size

    # Insert item
    def add(self, item):
        h1 = self.hash1(item)
        h2 = self.hash2(item)

        self.bit_array[h1] = 1
        self.bit_array[h2] = 1

    # Check membership
    def check(self, item):
        h1 = self.hash1(item)
        h2 = self.hash2(item)

        if self.bit_array[h1] == 1 and self.bit_array[h2] == 1:
            return "Possibly Present"
        else:
            return "Definitely Not Present"


# Main
bf = BloomFilter(10)

n = int(input("Enter number of items to insert: "))
print("Enter items:")

for _ in range(n):
    item = input()
    bf.add(item)

print("Bit array:", bf.bit_array)

q = int(input("Enter number of queries: "))

for _ in range(q):
    item = input("Enter item to check: ")
    print(item, "->", bf.check(item)) 
    