class TreeNode:
    """
    Simple binary tree node: value, left, right.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root):
    """
    Return True if the binary tree rooted at `root` is height-balanced.
    """

    def check(node):
        """
        Returns (is_balanced, height)
        - If unbalanced: return (False, 0)
        """
        if node is None:
            return True, 0  # empty tree → balanced, height = 0

        left_bal, left_height = check(node.left)
        if not left_bal:
            return False, 0

        right_bal, right_height = check(node.right)
        if not right_bal:
            return False, 0

        # Check current node balance
        if abs(left_height - right_height) > 1:
            return False, 0

        # Height of this subtree
        return True, max(left_height, right_height) + 1

    balanced, _ = check(root)
    return balanced
