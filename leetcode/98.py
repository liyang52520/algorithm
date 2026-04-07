# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        node_stack = []
        node = root
        inorder = []
        while len(node_stack) or node is not None:
            if node is not None:
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop(-1)
                if not len(inorder) or node.val > inorder[-1]:
                    inorder.append(node.val)
                else:
                    return False
                node = node.right
        return True

    def isValidBST_(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_balance, max_left, min_left = self.do_is_valid_bst(root.left)
        if left_balance and max_left < root.val:
            right_balance, max_right, min_right = self.do_is_valid_bst(root.right)
            if right_balance and min_right > root.val:
                return True
        return False

    def do_is_valid_bst(self, root):
        if root is None:
            return True, float("-inf"), float("inf")

        if root.left is None and root.right is None:
            return True, root.val, root.val

        left_balance, max_left, min_left = self.do_is_valid_bst(root.left)
        if left_balance and max_left < root.val:
            right_balance, max_right, min_right = self.do_is_valid_bst(root.right)
            if right_balance and min_right > root.val:
                return True, max(max_right, root.val), min(root.val, min_left)
        return False, 0, 0
