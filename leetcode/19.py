class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # head is none
        if head is None:
            return None

        right_node = head
        count = 0
        while count < n:
            right_node = right_node.next
            count += 1

        # if head is last n node, we delete head
        if right_node is None:
            return head.next

        left_node = head
        pre_left_node = None

        while right_node is not None:
            right_node = right_node.next
            pre_left_node = left_node
            left_node = left_node.next
        pre_left_node.next = left_node.next
        return head
