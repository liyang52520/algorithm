# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node_stack = []
        node = root
        inorder = []

        result = []
        max_count = 0
        cur_count = 0
        while len(node_stack) or node is not None:
            if node is not None:
                node_stack.append(node)
                node = node.left
            else:
                node = node_stack.pop(-1)
                if len(inorder) and node.val != inorder[-1]:
                    if cur_count == max_count:
                        result.append(inorder[-1])
                    elif cur_count > max_count:
                        result = [inorder[-1]]
                        max_count = cur_count
                    cur_count = 1
                else:
                    cur_count += 1
                inorder.append(node.val)
                node = node.right
        if cur_count == max_count:
            result.append(inorder[-1])
        elif cur_count > max_count:
            result = [inorder[-1]]
        return result
