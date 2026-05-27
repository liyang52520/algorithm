package org.yg.algorithm.leetcode;

public class LeetCode538 {

    public static class Solution {

        int preSum = 0;

        public TreeNode convertBST(TreeNode root) {
            if (root == null) {
                return null;
            }
            convertBST(root.right);
            preSum += root.val;
            root.val = preSum;
            convertBST(root.left);
            return root;
        }

    }

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
}