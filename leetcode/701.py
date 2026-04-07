# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        node = root
        while True:
            if node.val > val:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = TreeNode(val=val)
                    break
            elif node.val < val:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = TreeNode(val=val)
                    break
        return root
