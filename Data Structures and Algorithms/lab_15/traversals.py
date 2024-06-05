class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node is not None:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')

root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(13)


print("Прямой рекурсивный обход бинарного дерева:")
preorder(root)

print("\nЦентральный рекурсивный обход бинарного дерева:")
inorder(root)

print("\nКонцевой рекурсивный обход бинарного дерева:")
postorder(root)
