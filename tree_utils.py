def find_largest_value(root):
    if root is None:
        return None

    while root.right is not None:
        root = root.right

    return root.key

def find_smallest_value(root):
    if root is None:
        return None

    while root.left is not None:
        root = root.left

    return root.key

def sum_of_values(root):
    if root is None:
        return 0

    return sum_of_values(root.left) + root.key + sum_of_values(root.right)
