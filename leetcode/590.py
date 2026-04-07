"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []

        def do_postorder(node):
            if node is None:
                return
            for child in node.children:
                do_postorder(child)
            res.append(node.val)

        do_postorder(root)
        return res
