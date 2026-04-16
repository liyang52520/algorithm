package org.yg.algorithm.leetcode;

public class LeetCode24 {

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
        public ListNode swapPairs(ListNode head) {
            if (head == null || head.next == null) {
                return head;
            }

            ListNode fakeHead = new ListNode();
            fakeHead.next = head;

            ListNode pre = fakeHead, pointer1 = head, pointer2 = head.next;
            while (pointer1 != null && pointer2 != null) {
                // swap
                ListNode next = pointer2.next;
                pre.next = pointer2;
                pointer2.next = pointer1;
                pointer1.next = next;

                // next
                pre = pointer1;
                pointer1 = pre.next;
                if (pointer1 != null){
                    pointer2 = pointer2.next;
                } else {
                    pointer2 = null;
                }
            }
            return fakeHead.next;
        }
    }

    public static void main(String[] args) {
    }

}
