package org.yg.algorithm.leetcode;

import java.util.*;

public class LeetCode102 {
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
        public List<List<Integer>> levelOrder(TreeNode root) {
            if (root == null) {
                return Collections.emptyList();
            }

            Queue<TreeNode> nodeQueue = new LinkedList<>();
            nodeQueue.add(root);
            List<List<Integer>> res = new ArrayList<>();
            while (!nodeQueue.isEmpty()) {
                int levelSize = nodeQueue.size();
                List<Integer> levelRes = new ArrayList<>();
                for (int i = 0; i < levelSize; i++) {
                    TreeNode node = nodeQueue.remove();
                    if (node.left != null) {
                        nodeQueue.add(node.left);
                    }
                    if (node.right != null) {
                        nodeQueue.add(node.right);
                    }
                    levelRes.add(node.val);
                }
                res.add(levelRes);
            }
            return res;
        }
    }
}
