package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class LeetCode145 {
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
        public List<Integer> postorderTraversal(TreeNode root) {

            if (root == null) {
                return new ArrayList<>();
            }

            List<Integer> res = new ArrayList<>();

            Stack<TreeNode> nodeStack = new Stack<>();
            nodeStack.add(root);

            while (!nodeStack.isEmpty()) {
                TreeNode node = nodeStack.pop();
                res.add(0, node.val);
                if (node.left != null) {
                    nodeStack.push(node.left);
                }

                if (node.right != null) {
                    nodeStack.push(node.right);
                }
            }

            return res;
        }
    }
}
