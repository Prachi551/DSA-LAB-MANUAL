# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert into BST
def insert(root, key):
    if root is None:
        return Node(key)
    
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root

# Inorder Traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Search in BST
def search(root, key):
    if root is None:
        return False
    
    if root.data == key:
        return True
    
    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Main Program
if __name__ == "__main__":
    root = None
    
    n = int(input("Enter number of elements: "))
    elements = list(map(int, input("Enter elements: ").split()))
    
    for x in elements:
        root = insert(root, x)
    
    print("Inorder Traversal:", end=" ")
    inorder(root)
    
    key = int(input("\nEnter element to search: "))
    
    if search(root, key):
        print("Element Found")
    else:
        print("Element Not Found")