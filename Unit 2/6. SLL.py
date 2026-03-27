# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack using Linked List (head = top)
class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    # Pop operation
    def pop(self):
        if self.top is None:
            return None
        val = self.top.data
        self.top = self.top.next
        return val

    # Peek operation
    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    # Check if empty
    def is_empty(self):
        return self.top is None


# Function to validate brackets
def is_valid_brackets(string):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in string:
        # If opening bracket → push
        if ch in "({[":
            stack.push(ch)

        # If closing bracket → check
        elif ch in ")}]":
            if stack.is_empty():
                return False
            top = stack.pop()
            if pairs[ch] != top:
                return False

    return stack.is_empty()


# -------------------------------
# Driver Code (Lab Testing)

test_cases = [
    "()",
    "([])",
    "{[()]}",
    "([)]",
    "((()",
    "[]{}()",
    "{[(])}"
]

for s in test_cases:
    print(f"{s} -> {is_valid_brackets(s)}")