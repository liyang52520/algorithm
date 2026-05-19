package org.yg.algorithm.leetcode;

public class LeetCode101 {
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
        public boolean isSymmetric(TreeNode root) {
            // 检查左右子树是否完全相同
            TreeNode left = root.left;
            TreeNode right = root.right;
            return checkTreeSame(left, right);
        }

        public boolean checkTreeSame(TreeNode treeNode1, TreeNode treeNode2) {
            if (treeNode1 == null && treeNode2 == null) {
                return true;
            }

            if (treeNode1 == null || treeNode2 == null) {
                return false;
            }

            if (treeNode1.val != treeNode2.val) {
                return false;
            }

            return checkTreeSame(treeNode1.left, treeNode2.right) && checkTreeSame(treeNode1.right, treeNode2.left);
        }
    }
}
