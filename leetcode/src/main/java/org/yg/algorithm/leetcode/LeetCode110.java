package org.yg.algorithm.leetcode;

public class LeetCode110 {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static class Solution {
        public boolean isBalanced(TreeNode root) {
            if (root == null) {
                return true;
            }
            int left = getDepth(root.left);
            int right = getDepth(root.right);
            if (left == -1 || right == -1) {
                return false;
            }
            return Math.abs(left - right) <= 1;
        }

        public int getDepth(TreeNode root) {
            if (root == null) {
                return 0;
            }

            int left = getDepth(root.left);
            int right = getDepth(root.right);
            if (left == -1 || right == -1) {
                return -1;
            }
            if (Math.abs(left - right) > 1) {
                return -1;
            }
            return 1 + Math.max(left, right);
        }
    }
}
