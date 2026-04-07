class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        node_queue = [root]
        depth = 0
        while len(node_queue):
            depth += 1
            layer_len = len(node_queue)
            for i in range(layer_len):
                node = node_queue.pop(0)
                if node.left is not None:
                    node_queue.append(node.left)
                if node.right is not None:
                    node_queue.append(node.right)
                if node.left is None and node.right is None:
                    return depth