# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left, right = root.left, root.right
        left_height, right_height = 0, 0
        while left is not None:
            left = left.left
            left_height += 1
        while right is not None:
            right = right.right
            right_height += 1

        if left_height == right_height:
            return (2 << left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
