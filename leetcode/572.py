# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        def compare(root_1, root_2):
            if root_1 is None and root_2 is None:
                return True
            if root_1 is None or root_2 is None:
                return False
            if root_1.val == root_2.val:
                return compare(root_1.left, root_2.left) and compare(root_1.right, root_2.right)
            return False

        node_stack = [root]
        while len(node_stack):
            root = node_stack.pop(0)
            if compare(root, subRoot):
                return True
            if root.left is not None:
                node_stack.append(root.left)
            if root.right is not None:
                node_stack.append(root.right)
        return False
