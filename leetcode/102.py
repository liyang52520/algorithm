# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        node_queue = [root]
        while len(node_queue):
            layer_len = len(node_queue)
            layer_res = []
            for i in range(layer_len):
                node = node_queue.pop(0)
                layer_res.append(node.val)
                if node.left is not None:
                    node_queue.append(node.left)
                if node.right is not None:
                    node_queue.append(node.right)
            res.append(layer_res)
        return res
