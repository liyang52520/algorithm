# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def check_tree(self, root):
        """

        Args:
            root (TreeNode):

        Returns:

        """
        if root is None:
            return True, 0
        left_balanced, left_height = self.check_tree(root.left)

        if left_balanced:
            right_balanced, right_height = self.check_tree(root.right)
            if right_balanced and abs(left_height - right_height) <= 1:
                return True, max(left_height, right_height) + 1
            return False, 0
        return False, 0

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_balanced, _ = self.check_tree(root)
        return is_balanced
