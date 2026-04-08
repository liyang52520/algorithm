package org.yg.algorithm.leetcode;

public class Leetcode203 {

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
        public ListNode removeElements(ListNode head, int val) {
            ListNode fakeHead = new ListNode(-1, head);

            ListNode preNode = fakeHead;
            ListNode curNode = fakeHead.next;
            while (curNode != null) {
                if (curNode.val != val) {
                    if (preNode.next != curNode) {
                        preNode.next = curNode;
                    }
                    preNode = curNode;
                }

                curNode = curNode.next;
            }

            if (preNode.next != null && preNode.next.val == val) {
                preNode.next = null;
            }

            return fakeHead.next;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = new int[]{1, 2, 6, 3, 4, 5, 6};
        ListNode fakeHead = new ListNode();
        ListNode preNode = fakeHead;
        for (int num: nums){
            ListNode node = new ListNode(num);
            preNode.next = node;
            preNode = node;
        }
        System.out.println(solution.removeElements(fakeHead.next, 6));
    }

}
