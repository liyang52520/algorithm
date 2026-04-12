package org.yg.algorithm.leetcode;

public class Leetcode19 {

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
    }

    public static class Solution {
        public ListNode removeNthFromEnd(ListNode head, int n) {
            ListNode fakeHead = new ListNode();
            fakeHead.next = head;

            ListNode right = fakeHead;
            for (int i = 0; i <= n; i++) {
                right = right.next;
            }

            ListNode leftPre = fakeHead;
            while (right != null) {
                right = right.next;
                leftPre = leftPre.next;
            }
            assert leftPre != null;
            if (leftPre.next != null) {
                leftPre.next = leftPre.next.next;
            }
            return fakeHead.next;
        }
    }

    public static void main(String[] args) {
    }

}
