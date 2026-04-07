# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        res = []
        node = root
        nodes = []
        while node is not None or len(nodes):
            if node is not None:
                nodes.append(node)
                node = node.left
            else:
                node = nodes.pop(-1)
                res.append(node.val)
                node = node.right
        return res