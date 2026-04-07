class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def build_tree(cls, tree_values):
        """

        Args:
            tree_values (list):

        Returns:

        """
        # create tree nodes
        nodes = []
        for value in tree_values:
            nodes.append(cls(value))
        # link nodes as tree
        for i in range(len(tree_values) // 2):
            left = i * 2 + 1
            right = i * 2 + 2
            if left < len(tree_values):
                nodes[i].left = nodes[left]
                if right < len(tree_values):
                    nodes[i].right = nodes[right]
        return nodes[0]


if __name__ == '__main__':
    tree = BinaryTreeNode.build_tree([3, 4, 5, 6])
