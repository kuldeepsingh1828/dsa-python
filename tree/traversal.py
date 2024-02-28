class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.key, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key, end=" ")

# Example usage:
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(2)
    root.right = Node(13)
    root.left.left = Node(1)
    root.left.right = Node(6)

    #Left->Root->right
    print("Inorder Traversal:")
    inorder_traversal(root)  # Output: 4 2 5 1 3
    print("\n")

    #Root->Left->right
    print("Preorder Traversal:")
    preorder_traversal(root)  # Output: 1 2 4 5 3
    print("\n")

    #Left->right->root
    print("Postorder Traversal:")
    postorder_traversal(root)  # Output: 4 5 2 3 1
