# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
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
                if node.children is not None:
                    for child in node.children:
                        if child is not None:
                            node_queue.append(child)
            res.append(layer_res)
        return res
