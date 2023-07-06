class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        min_key = find_min_key(root.right)
        root.key = min_key
        root.right = delete(root.right, min_key)
    return root

def find_min_key(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key)
        inorder_traversal(root.right)

# Example usage
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal:")
inorder_traversal(root)

print("Deleting node with key 30:")
root = delete(root, 30)

print("Inorder traversal after deletion:")
inorder_traversal(root)
