class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def deleteNode(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = deleteNode(root.left, value)
    elif value > root.value:
        root.right = deleteNode(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.value = temp.value
        root.right = deleteNode(root.right, temp.value)
    return root


def search(root, value):
    if root is None or root.value == value:
        return root
    if root.value < value:
        return search(root.right, value)
    return search(root.left, value)


def inOrderTraversal(root):
    result = []
    if root:
        result = inOrderTraversal(root.left)
        result.append(root.value)
        result = result + inOrderTraversal(root.right)
    return result


def printTree(root):
    if root:
        print("(" + str(root.value), end="")
        if root.left is not None or root.right is not None:
            print(" ", end="")
            printTree(root.left)
            print(" ", end="")
            printTree(root.right)
        print(")", end="")
    else:
        print("()", end="")


def main():
    tree = None
    while True:
        print("\nМеню:")
        print("1. Добавить вершину")
        print("2. Удалить вершину")
        print("3. Найти вершину")
        print("4. Вывести БДП")
        print("5. Выход")

        choice = int(input("Выберите операцию (1-5): "))

        if choice == 1:
            value = int(input("Введите значение вершины для добавления: "))
            tree = insert(tree, value)
            print("Вершина добавлена успешно.")
        elif choice == 2:
            value = int(input("Введите значение вершины для удаления: "))
            tree = deleteNode(tree, value)
            print("Вершина удалена успешно.")
        elif choice == 3:
            value = int(input("Введите значение вершины для поиска: "))
            if search(tree, value) is not None:
                print("Вершина найдена.")
            else:
                print("Вершина не найдена.")
        elif choice == 4:
            print("БДП:", end=" ")
            printTree(tree)
            print()
        elif choice == 5:
            printTree(tree)
            print("\nПрограмма завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()