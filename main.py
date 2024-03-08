from AVL_tree import insert
from tree_utils import find_largest_value, find_smallest_value, sum_of_values

if __name__ == "__main__":
    avl_root = None
    avl_values = [10, 5, 15, 12, 20, 13, 23, 9, 27, 11, 25]

    for value in avl_values:
        avl_root = insert(avl_root, value)

    largest_value_avl = find_largest_value(avl_root)
    smalest_value_avl = find_smallest_value(avl_root)
    total_sum_avl = sum_of_values(avl_root)

    print("Найбільше значення у AVL-дереві:", largest_value_avl)
    print("Найменше значення у AVL-дереваі:", smalest_value_avl)
    print("Сума значеннь AVL-дерева:", total_sum_avl)
