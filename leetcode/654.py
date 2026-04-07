# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        max_idx, max_num = max(enumerate(nums), key=lambda x: x[1])
        root = TreeNode(val=max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])
        return root


if __name__ == '__main__':
    Solution().constructMaximumBinaryTree(
        [3, 2, 1, 6, 0, 5])
