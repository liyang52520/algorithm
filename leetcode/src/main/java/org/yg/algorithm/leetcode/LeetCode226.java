package org.yg.algorithm.leetcode;

import java.util.*;

public class LeetCode226 {
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
        public TreeNode invertTree(TreeNode root) {
            if (root == null) {
                return null;
            }
            TreeNode leftNode = root.left;
            TreeNode rightNode = root.right;
            root.right = invertTree(leftNode);
            root.left = invertTree(rightNode);
            return root;
        }
    }
}
