class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end (helper function)
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert after a given target value
    def insert_after_node(self, target, x):
        temp = self.head

        while temp:
            if temp.data == target:
                new_node = Node(x)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return

            temp = temp.next

        print("Target not found")

    # Delete node at given position (0-based index)
    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # Deleting head node
        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        # Traverse to position
        for i in range(pos):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        # Update links
        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# ------------------ TEST ------------------

dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)

print("Initial List:")
dll.display()

dll.insert_after_node(20, 25)
print("After inserting 25 after 20:")
dll.display()

dll.delete_at_position(2)
print("After deleting at position 2:")
dll.display()