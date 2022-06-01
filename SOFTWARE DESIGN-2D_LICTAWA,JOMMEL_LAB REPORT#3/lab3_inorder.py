class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data
        
def inord(root):
    
    if root:
        inord(root.left)
        print(root.val)
        inord(root.right)

def count(root):
    if root is None:
        return 0
    else: 
        return 1 + count(root.left) + count(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Nodes in In order Traversal: ")
inord(root)

print("\nThe number of nodes are: ", str(count(root)))

