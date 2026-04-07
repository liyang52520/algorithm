# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        res = 0
        node_stack = [root]
        while len(node_stack):
            node = node_stack.pop(-1)
            if node.left is not None and node.left.left is None and node.left.right is None:
                res += node.left.val
            if node.left is not None:
                node_stack.append(node.left)
            if node.right is not None:
                node_stack.append(node.right)
        return res
