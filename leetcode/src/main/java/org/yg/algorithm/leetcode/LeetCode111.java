package org.yg.algorithm.leetcode;

public class LeetCode111 {
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
        public int minDepth(TreeNode root) {
            // leaf node
            if (root.left == null && root.right == null) {
                return 1;
            }

            if (root.left == null) {
                return 1 + minDepth(root.right);
            }
            if (root.right == null) {
                return 1 + minDepth(root.left);
            }
            return 1 + Math.min(minDepth(root.left), minDepth(root.right));
        }
    }
}
