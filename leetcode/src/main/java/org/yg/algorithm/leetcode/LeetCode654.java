package org.yg.algorithm.leetcode;

import java.util.Stack;

public class LeetCode654 {
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

        public TreeNode constructMaximumBinaryTree(int[] nums) {
            if (nums.length == 0) {
                return null;
            }

            // 我觉得可以有更漂亮的方法，比如单调栈
            Stack<TreeNode> nodeStack = new Stack<>();
            TreeNode node = new TreeNode(nums[0]);
            nodeStack.add(node);
            TreeNode root = node;
            int maxVal = node.val;

            for (int i = 1; i < nums.length; i++) {
                TreeNode curNode = new TreeNode(nums[i]);
                // update root node
                if (nums[i] > maxVal) {
                    maxVal = nums[i];
                    root = curNode;
                }

                // update node
                while (!nodeStack.isEmpty() && nodeStack.peek().val < curNode.val) {
                    curNode.left = nodeStack.pop();
                }
                if (!nodeStack.isEmpty()) {
                    nodeStack.peek().right = curNode;
                }
                nodeStack.add(curNode);
            }


            return root;
        }

    }
}
