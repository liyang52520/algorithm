# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        node_stack = [root]
        while len(node_stack):
            node = node_stack.pop(-1)
            res.append(node.val)
            if node.left is not None:
                node_stack.append(node.left)
            if node.right is not None:
                node_stack.append(node.right)
        res.reverse()
        return res
