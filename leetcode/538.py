# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        inorder = []
        node_stack = []
        node = root
        pre_sum = 0
        while node is not None or len(node_stack):
            if node is not None:
                node_stack.append(node)
                node = node.right
            else:
                node = node_stack.pop(-1)
                inorder.append(node.val)
                node.val = pre_sum + node.val
                pre_sum = node.val
                node = node.left
        return root
