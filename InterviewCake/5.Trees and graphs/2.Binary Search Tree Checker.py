import unittest


# my own
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_binary_search_tree(root):
    def in_order(node):
        if not node:
            return

        in_order(node.left)
        values.append(node.value)
        in_order(node.right)

    values = []
    in_order(root)

    for i in range(1, len(values)):
        if values[i - 1] > values[i]:
            return False

    return True

# their iterative
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_binary_search_tree(root):
    # Start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    node_and_bounds_stack = [(root, float('-inf'), float('inf'))]

    # Depth-first traversal
    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()


# their recursive
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_binary_search_tree(node, lower_bound=float('-inf'), upper_bound=float('inf')):
    if not node:
        return True

    if node.value >= upper_bound or node.value <= lower_bound:
        return False

    left = is_binary_search_tree(node=node.left, lower_bound=lower_bound, upper_bound=node.value)
    right = is_binary_search_tree(node=node.right, lower_bound=node.value, upper_bound=upper_bound)

    return all([left, right])


class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

        def __str__(self):
            return f'{self.value}'

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)
