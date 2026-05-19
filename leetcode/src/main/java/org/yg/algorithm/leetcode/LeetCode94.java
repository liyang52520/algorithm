package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class LeetCode94 {
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
        public List<Integer> inorderTraversal(TreeNode root) {
            if (root == null) {
                return new ArrayList<>();
            }

            List<Integer> res = new ArrayList<>();

            Stack<TreeNode> nodeStack = new Stack<>();

            while (root != null || !nodeStack.isEmpty()) {
                if (root != null) {
                    nodeStack.push(root);
                    root = root.left;
                } else {
                    TreeNode node = nodeStack.pop();
                    res.add(node.val);
                    root = node.right;
                }
            }

            return res;
        }
    }
}
