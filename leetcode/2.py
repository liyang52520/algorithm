# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # compute first
        temp = l1.val + l2.val
        up = temp // 10
        local = temp % 10
        res_node = ListNode(local)
        head = res_node
        # next
        l1 = l1.next
        l2 = l2.next
        while l1 is not None and l2 is not None:
            #
            temp = l1.val + l2.val + up
            up = temp // 10
            local = temp % 10

            res_node.next = ListNode(local)
            res_node = res_node.next

            # next
            l1 = l1.next
            l2 = l2.next

        if l1 is None:
            l1 = l2

        while l1 is not None:
            temp = l1.val + up
            up = temp // 10
            local = temp % 10

            res_node.next = ListNode(local)
            res_node = res_node.next

            l1 = l1.next

        if up > 0:
            res_node.next = ListNode(up)

        return head
