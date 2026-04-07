# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0:
            return None
        if len(postorder) == 1:
            return TreeNode(val=postorder[0])
        root_val = postorder[-1]
        root = TreeNode(val=root_val)
        # split inorder and postorder
        root_idx = inorder.index(root_val)
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx + 1:], postorder[root_idx:-1])
        return root


if __name__ == '__main__':
    Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
