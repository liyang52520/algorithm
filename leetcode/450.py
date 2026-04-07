class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            # max node in left tree or min node in right tree, not assure leaf node
            if root.left is not None:
                node_parent = root
                node = root.left
                while True:
                    if node.right is not None:
                        node_parent = node
                        node = node.right
                    else:
                        break
                if node_parent.val == key:
                    node.right = node_parent.right
                else:
                    node_parent.right = node.left
                    node.left = root.left
                    node.right = root.right
            else:
                node_parent = root
                node = root.right
                while True:
                    if node.left is not None:
                        node_parent = node
                        node = node.left
                    else:
                        break
                if node_parent.val == key:
                    node.left = node_parent.left
                else:
                    node_parent.left = node.right
                    node.left = root.left
                    node.right = root.right

            return node

        if root.left is None and root.right is None:
            return root

        if root.left is not None:
            root.left = self.deleteNode(root.left, key)

        if root.right is not None:
            root.right = self.deleteNode(root.right, key)

        return root
