class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def iterative_postorder(root):
    stack = []
    if root is None:
        return
    stack.append(root)
    while len(stack) != 0:
        node = stack.pop()
        print(node.value, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(13)

print("Не рекурсивный прямой обход бинарного дерева:")
iterative_postorder(root)
