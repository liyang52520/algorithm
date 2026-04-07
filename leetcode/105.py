# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(val=preorder[0])
        root_val = preorder[0]
        root = TreeNode(val=root_val)
        # split inorder and postorder
        root_idx = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:root_idx + 1],inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx + 1:],inorder[root_idx + 1:])
        return root


if __name__ == '__main__':
    Solution().buildTree([3, 9, 20, 15, 7],
                         [9, 3, 15, 20, 7])
