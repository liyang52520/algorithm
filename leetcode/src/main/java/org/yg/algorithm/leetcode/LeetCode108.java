package org.yg.algorithm.leetcode;

public class LeetCode108 {
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
        public TreeNode sortedArrayToBST(int[] nums) {
            return sortedArrayToBST(nums, 0, nums.length - 1);
        }

        /**
         * 左闭右闭
         */
        public TreeNode sortedArrayToBST(int[] nums, int low, int high) {
            if (low > high) {
                return null;
            }
            int mid = low + (high - low) / 2;
            TreeNode root = new TreeNode(nums[mid]);
            root.left = sortedArrayToBST(nums, low, mid - 1);
            root.right = sortedArrayToBST(nums, mid + 1, high);
            return root;
        }
    }
}
