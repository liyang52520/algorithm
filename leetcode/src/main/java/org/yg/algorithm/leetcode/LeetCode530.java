package org.yg.algorithm.leetcode;

import java.util.Map;
import java.util.Stack;

public class LeetCode530 {
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

        public int getMinimumDifference(TreeNode root) {
            // 树中节点的数目范围是 [2, 104]
            TreeNode curNode = root;
            Stack<TreeNode> nodeStack = new Stack<>();
            boolean flag = false;
            int preNum = 0;
            int minGap = Integer.MAX_VALUE;
            while (curNode != null || !nodeStack.isEmpty()) {
                if (curNode != null) {
                    nodeStack.add(curNode);
                    curNode = curNode.left;
                } else {
                    curNode = nodeStack.pop();
                    if (flag) {
                        minGap = Math.min(minGap, curNode.val - preNum);
                    }
                    preNum = curNode.val;
                    curNode = curNode.right;
                    flag = true;
                }
            }
            return minGap;
        }
    }
}
