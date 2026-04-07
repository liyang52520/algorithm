# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root

        node_queue = [root]
        while len(node_queue):
            layer_len = len(node_queue)
            layer_res = []
            for i in range(layer_len):
                node = node_queue.pop(0)
                if len(layer_res):
                    layer_res[-1].next = node
                layer_res.append(node)
                if node.left is not None:
                    node_queue.append(node.left)
                if node.right is not None:
                    node_queue.append(node.right)

        return root
