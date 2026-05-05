class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


# Find inorder successor
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


# Delete
def delete_node(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete_node(root.left, key)

    elif key > root.data:
        root.right = delete_node(root.right, key)

    else:
        # Case 1: Leaf
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        elif root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        # Case 3: Two children
        successor = min_value_node(root.right)
        root.data = successor.data
        root.right = delete_node(root.right, successor.data)

    return root


# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Main
if __name__ == "__main__":
    root = None

    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))

    for x in arr:
        root = insert(root, x)

    print("Initial Inorder:", end=" ")
    inorder(root)
    print()

    d = int(input("Enter number of deletions: "))

    for i in range(d):
        key = int(input("Enter value to delete: "))
        root = delete_node(root, key)

        print("Inorder after deletion:", end=" ")
        inorder(root)
        print()