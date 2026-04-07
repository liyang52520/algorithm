class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def __init__(self):
        self.node_set = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        if head in self.node_set:
            return head

        new_node = Node(head.val)
        self.node_set[new_node] = new_node
        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)
        return new_node


if __name__ == '__main__':
    node_1 = Node(7)
    node_2 = Node(13)
    node_3 = Node(11)
    node_4 = Node(10)
    node_5 = Node(1)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    node_2.random = node_1
    node_3.random = node_5
    node_4.random = node_3
    node_5.random = node_1

    print(Solution().copyRandomList(node_1))