package org.yg.algorithm.leetcode;

public class LeetCode450 {
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

        public TreeNode deleteNode(TreeNode root, int key) {
            if (root == null) {
                return null;
            }
            if (root.val > key) {
                root.left = deleteNode(root.left, key);
                return root;
            } else if (root.val < key) {
                root.right = deleteNode(root.right, key);
                return root;
            }

            // root.val == key
            if (root.left == null && root.right == null) {
                return null;
            }
            if (root.left == null) {
                return root.right;
            }
            if (root.right == null) {
                return root.left;
            }
            // left 和 right 都不是 null，就得开始合并了，需要把这个key给干掉，然后返回一个新的根 root 回去
            TreeNode rightNode = root.right;
            TreeNode leftNode = root.left;
            TreeNode temp = rightNode.left;
            if (temp != null) {
                // 把 temp 放在 left Node 的最右侧
                TreeNode leftRightMaxPreNode = leftNode;
                while (leftRightMaxPreNode.right != null) {
                    leftRightMaxPreNode = leftRightMaxPreNode.right;
                }
                leftRightMaxPreNode.right = temp;
            }
            rightNode.left = leftNode;

            return rightNode;
        }
    }
}
