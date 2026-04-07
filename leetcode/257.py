# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def search_path(self, root, pre_path):
        """

        Args:
            root:
            pre_path:

        Returns:

        """
        if root is None:
            return []

        if pre_path != "":
            current_path = "{}->{}".format(pre_path, root.val)
        else:
            current_path = "{}".format(root.val)

        if root.left is None and root.right is None:
            return [current_path]

        left_res = self.search_path(root.left, current_path)
        right_res = self.search_path(root.right, current_path)
        return left_res + right_res

    def binaryTreePaths_(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.search_path(root, "")

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []

        node_stack = [root]
        path_stack = [str(root.val)]
        results = []
        while len(node_stack):
            cur = node_stack.pop(0)
            cur_path = path_stack.pop(0)
            if cur.left is None and cur.right is None:
                results.append(cur_path)
                continue
            if cur.left is not None:
                node_stack.append(cur.left)
                path_stack.append("{}->{}".format(cur_path, cur.left.val))
            if cur.right is not None:
                node_stack.append(cur.right)
                path_stack.append("{}->{}".format(cur_path, cur.right.val))
        return results
