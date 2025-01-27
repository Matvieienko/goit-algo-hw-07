class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функція для вставки нового ключа в дерево
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Завдання 1: Знайти найбільше значення
def find_max(root):
    if root is None:
        return None  # Якщо дерево порожнє
    while root.right:
        root = root.right
    return root.key

# Завдання 2: Знайти найменше значення
def find_min(root):
    if root is None:
        return None  # Якщо дерево порожнє
    while root.left:
        root = root.left
    return root.key

# Завдання 3: Знайти суму всіх значень
def find_sum(root):
    if root is None:
        return 0  # Якщо дерево порожнє
    return root.key + find_sum(root.left) + find_sum(root.right)

# Основна програма
if __name__ == "__main__":
    root = None
    # Додаємо елементи в дерево
    keys = [20, 8, 22, 4, 12, 10, 14, 2, 30]
    for key in keys:
        root = insert(root, key)

    # Викликаємо функції для всіх завдань
    max_value = find_max(root)
    min_value = find_min(root)
    total_sum = find_sum(root)

    # Виводимо результати
    print("Найбільше значення у дереві:", max_value)
    print("Найменше значення у дереві:", min_value)
    print("Сума всіх значень у дереві:", total_sum)