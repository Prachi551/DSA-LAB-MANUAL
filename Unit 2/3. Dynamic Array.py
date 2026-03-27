class DynamicArray:
    def __init__(self):
        self.size = 0              # number of elements
        self.capacity = 1          # initial capacity
        self.arr = [None] * self.capacity

    # Resize function (double capacity)
    def resize(self):
        print(f"Resizing: {self.capacity} -> {self.capacity * 2}")
        self.capacity *= 2
        new_arr = [None] * self.capacity

        # Copy old elements
        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    # Append operation
    def append(self, value):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = value
        self.size += 1
        print(f"After append({value}): size={self.size}, capacity={self.capacity}")

    # Pop operation
    def pop(self):
        if self.size == 0:
            print("Array is empty, cannot pop")
            return None

        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        print(f"After pop(): size={self.size}, capacity={self.capacity}")
        return val

    # Display elements
    def display(self):
        print("Array:", self.arr[:self.size])


# -------------------------------
# Driver Code (Lab Simulation)

da = DynamicArray()

# Sample operations
da.append(10)
da.append(20)
da.append(30)
da.append(40)   # should trigger resize
da.append(50)

da.pop()
da.pop()

da.display()