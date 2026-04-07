# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        node_stack = []
        node = root
        inorder = []
        min_gap = float("inf")
        while len(node_stack) or node is not None:
            if node is not None:
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop(-1)
                if not len(inorder):
                    min_gap = min(min_gap, abs(node.val - inorder[-1]))
                inorder.append(node.val)
                node = node.right
        return min_gap
