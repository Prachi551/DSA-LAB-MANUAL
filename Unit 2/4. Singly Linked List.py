# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print(f"After insert_beginning({value}): ", end="")
        self.traverse()

    # Insert at end
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print(f"After insert_end({value}): ", end="")
        self.traverse()

    # Delete by value
    def delete_value(self, value):
        if self.head is None:
            print("List is empty, cannot delete")
            return

        # If head node needs to be deleted
        if self.head.data == value:
            self.head = self.head.next
            print(f"After delete({value}): ", end="")
            self.traverse()
            return

        # Search for node
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next

        # Value not found
        if temp.next is None:
            print(f"Value {value} not found")
            return

        # Delete node
        temp.next = temp.next.next
        print(f"After delete({value}): ", end="")
        self.traverse()

    # Traverse and print list
    def traverse(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -------------------------------
# Driver Code (Lab Simulation)

sll = SinglyLinkedList()

sll.insert_beginning(10)
sll.insert_beginning(5)
sll.insert_end(20)
sll.insert_end(30)

sll.delete_value(20)
sll.delete_value(100)   # not present
sll.delete_value(5) 