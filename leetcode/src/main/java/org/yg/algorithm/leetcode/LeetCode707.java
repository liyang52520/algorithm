package org.yg.algorithm.leetcode;

public class LeetCode707 {

    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }

        @Override
        public String toString() {
            return String.format("val: %d, next: %s", val, next);
        }
    }


    public static class MyLinkedList {

        /**
         * 节点总数
         */
        private int total = 0;

        /**
         * 头节点
         */
        private final ListNode head = new ListNode();

        /**
         * 尾节点
         */
        private ListNode tail;

        public MyLinkedList() {
        }

        public int get(int index) {
            if (index < 0 || index >= total) {
                return -1;
            }
            ListNode node = this.head;
            for (int i = 0; i <= index; i++) {
                node = node.next;
            }
            return node.val;
        }

        public void addAtHead(int val) {
            ListNode node = new ListNode(val, head.next);
            if (head.next == null) {
                tail = node;
            }
            head.next = node;
            total++;
        }

        public void addAtTail(int val) {
            if (tail == null) {
                addAtHead(val);
            } else {
                ListNode node = new ListNode(val);
                tail.next = node;
                tail = node;
                total++;
            }
        }

        public void addAtIndex(int index, int val) {
            if (index < 0 || index > total) {
                return;
            }

            if (index == total) {
                addAtTail(val);
                return;
            }

            ListNode node = this.head;
            for (int i = 0; i < index; i++) {
                node = node.next;
            }

            ListNode newNode = new ListNode(val);
            newNode.next = node.next;
            node.next = newNode;
            total++;
        }

        public void deleteAtIndex(int index) {
            if (index < 0 || index >= total) {
                return;
            }
            ListNode preNode = head;
            ListNode node = preNode.next;
            for (int i = 0; i < index; i++) {
                ListNode tmp = node;
                node = node.next;
                preNode = tmp;
            }

            preNode.next = node.next;
            if (index == total - 1) {
                tail = preNode;
            }
            total--;
        }

    }

    public static void main(String[] args) {
    }

}
