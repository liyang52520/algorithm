class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head

        pre_node = ListNode(next=head)

        # k nodes
        tail_node = pre_node
        k_nodes = []
        for i in range(k):
            k_nodes.append(tail_node.next)
            tail_node = tail_node.next

        return_node = k_nodes[-1]

        while True:
            # exchange those k nodes, 就是倒过来
            after_k_node = k_nodes[-1].next
            for i in range(k - 1, 0, -1):
                k_nodes[i].next = k_nodes[i - 1]
            k_nodes[0].next = after_k_node
            pre_node.next = k_nodes[-1]
            # update
            pre_node = k_nodes[0]
            k_nodes = []
            tail_node = pre_node
            for i in range(k):
                if tail_node.next is not None:
                    k_nodes.append(tail_node.next)
                    tail_node = tail_node.next
                else:
                    break
            if len(k_nodes) != k:
                break

        return return_node
