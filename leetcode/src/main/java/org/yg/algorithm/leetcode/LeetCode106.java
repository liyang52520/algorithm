package org.yg.algorithm.leetcode;

import java.util.Arrays;

public class LeetCode106 {
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
        public TreeNode buildTree(int[] inorder, int[] postorder) {
            int n = inorder.length;
            // 处理边界条件
            if (n == 0) {
                return null;
            }
            if (n == 1) {
                return new TreeNode(inorder[0]);
            }

            // 处理其他情况
            int root = postorder[n - 1];
            int rootIndex = 0;
            for (; rootIndex < n; rootIndex++) {
                if (inorder[rootIndex] == root) {
                    break;
                }
            }
            TreeNode node = new TreeNode(root);
            if (rootIndex > 0) {
                // left
                node.left = buildTree(Arrays.copyOfRange(inorder, 0, rootIndex),
                        Arrays.copyOfRange(postorder, 0, rootIndex));
            }
            if (rootIndex < n - 1) {
                // right
                node.right = buildTree(Arrays.copyOfRange(inorder, rootIndex + 1, n),
                        Arrays.copyOfRange(postorder, rootIndex, n - 1));
            }
            return node;
        }
    }
}
