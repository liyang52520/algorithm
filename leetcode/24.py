class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        pre_node = ListNode(next=head)


        first_node = head
        second_node = first_node.next
        return_node = second_node

        while first_node is not None and second_node is not None:
            # exchange
            pre_node.next = first_node.next
            first_node.next = second_node.next
            second_node.next = first_node
            # update
            pre_node = first_node
            first_node = pre_node.next
            if first_node is not None:
                second_node = first_node.next

        return return_node
