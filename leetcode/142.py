# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        # slow and fast
        slow = fast = head

        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
            else:
                break

            if slow == fast:
                # they meet
                scale = head
                while scale != slow:
                    scale = scale.next
                    slow = slow.next
                return slow

        return None

