package org.yg.algorithm.leetcode;

import java.util.LinkedList;
import java.util.Stack;

public class LeetCode98 {
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

        public boolean isValidBST(TreeNode root) {
            if (root == null) {
                return true;
            }

            // 非递归中序遍历
            TreeNode curNode = root;
            Stack<TreeNode> nodeStack = new Stack<>();

            int preNum = Integer.MIN_VALUE;
            boolean flag = false;
            while (curNode != null || !nodeStack.isEmpty()) {
                if (curNode != null) {
                    nodeStack.push(curNode);
                    curNode = curNode.left;
                } else {
                    TreeNode node = nodeStack.pop();
                    // do here
                    if (!flag || node.val > preNum) {
                        preNum = node.val;
                    } else {
                        return false;
                    }
                    flag = true;
                    curNode = node.right;
                }
            }
            return true;
        }
    }
}
