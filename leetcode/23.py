# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def generate(cls, data):
        """

        Args:
            data:

        Returns:

        """
        res = []
        for d in data:
            t_r = []
            for v in d:
                t_r.append(cls(v))
            for i in range(len(t_r) - 1):
                t_r[i].next = t_r[i + 1]
            res.append(t_r[0])
        return res

    def __repr__(self):
        return f"Node {self.val} and next is {self.next.val if self.next is not None else None}"


class Solution(object):
    def merge_two_list(self, l1, l2):
        """

        Args:
            list_1 (ListNode):
            list_2 (ListNode):

        Returns:

        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # choose head
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        tail = head

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next

        if l1 is None:
            tail.next = l2
        else:
            tail.next = l1

        return head

    def merge(self, lists, left, right):
        """

        Args:
            lists:
            left:
            right:

        Returns:

        """
        if left == right:
            return lists[left]
        if left > right:
            return None

        mid = int((right - left) / 2) + left

        left = self.merge(lists, left, mid)
        right = self.merge(lists, mid + 1, right)
        res = self.merge_two_list(left, right)

        return res

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) <= 1:
            return lists

        return self.merge(lists, 0, len(lists) - 1)


if __name__ == '__main__':
    data = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = ListNode.generate(data)
    print(Solution().mergeKLists(lists))
