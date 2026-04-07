from tree import BinaryTreeNode


def dfs(tree_node):
    """
    deep first search

    Args:
        tree_node (BinaryTreeNode):
            root node of tree

    Returns:

    """
    if tree_node is None:
        return
    print(tree_node.value)
    dfs(tree_node.left)
    dfs(tree_node.right)


def bfs(tree_node):
    """
    breadth first search

    Args:
        tree_node ():

    Returns:

    """
    pass


if __name__ == '__main__':
    tree_root = BinaryTreeNode.build_tree([3, 4, 5, 6])
    dfs(tree_root)
