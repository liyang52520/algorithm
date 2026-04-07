# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_depth = 0
        left_value = root.val
        node_stack = [(root, 0)]
        while len(node_stack):
            node, depth = node_stack.pop(-1)
            if node.left:
                if depth + 1 > left_depth:
                    left_value = node.left.val
                    left_depth = depth + 1
            if node.right:
                if depth + 1 > left_depth:
                    left_value = node.right.val
                    left_depth = depth + 1
            if node.right:
                node_stack.append((node.right, depth + 1))
            if node.left:
                node_stack.append((node.left, depth + 1))

        return left_value
