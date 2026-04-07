# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False

        # left: lcr, right: rcl
        left_stack = []
        right_stack = []
        left_node = root.left
        right_node = root.right
        while (left_node is not None or len(left_stack)) and (right_node is not None or len(right_stack)):
            if left_node is not None and right_node is not None:
                left_stack.append(left_node)
                right_stack.append(right_node)
                left_node = left_node.left
                right_node = right_node.right
            elif left_node is None and right_node is None:
                left_node = left_stack.pop(-1)
                right_node = right_stack.pop(-1)
                if left_node.val != right_node.val:
                    return False
                left_node = left_node.right
                right_node = right_node.left
            else:
                return False
        return True

    def isSymmetric_rec(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False

        # compare left and right
        return self.compare(root.left, root.right)

    def compare(self, root_1, root_2):
        """

        Args:
            root_1:
            root_2:

        Returns:

        """
        if root_1 is None and root_2 is None:
            return True
        if root_1 is None or root_2 is None:
            return False

        if root_1.val == root_2.val:
            return self.compare(root_1.left, root_2.right) and self.compare(root_1.right, root_2.left)
        return False
