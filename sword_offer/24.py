# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        pre = head
        cur = head.next
        head.next = None

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
