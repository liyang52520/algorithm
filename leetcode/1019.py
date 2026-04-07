from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # 单调栈，单调递减，（idx, val）
        descend_stack = []
        res = []
        idx = 0
        node = head
        while node is not None:
            res.append(0)
            while len(descend_stack) and descend_stack[-1][1] < node.val:
                node_idx, node_val = descend_stack.pop(-1)
                res[node_idx] = node.val
            descend_stack.append((idx, node.val))
            idx += 1
            node = node.next
        return res

