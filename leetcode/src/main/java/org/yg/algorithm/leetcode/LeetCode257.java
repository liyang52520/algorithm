package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode257 {
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
        public List<String> binaryTreePaths(TreeNode root) {
            List<String> res = new ArrayList<>();
            doBinaryTreePaths(root, "", res);
            return res;
        }

        public void doBinaryTreePaths(TreeNode root, String prePath, List<String> res) {
            String curPath = String.valueOf(root.val);
            if (!prePath.isEmpty()) {
                curPath = prePath + "->" + curPath;
            }
            if (root.left == null && root.right == null) {
                res.add(curPath);
                return;
            }
            if (root.left != null) {
                doBinaryTreePaths(root.left, curPath, res);
            }
            if (root.right != null) {
                doBinaryTreePaths(root.right, curPath, res);
            }
        }
    }
}
