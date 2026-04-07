# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        results = []

        def do_preorder(node):
            """

            Args:
                node:

            Returns:

            """
            if node is None:
                return
            results.append(node.val)
            for child in node.children:
                do_preorder(child)

        do_preorder(root)
        return results
