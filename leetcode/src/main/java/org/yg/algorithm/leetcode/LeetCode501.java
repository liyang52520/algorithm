package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class LeetCode501 {

    public static class Solution {

        public int[] findMode(TreeNode root) {
            List<Integer> res = new ArrayList<>();

            TreeNode cur = root;
            Stack<TreeNode> stack = new Stack<>();

            int curCount = 0;
            int maxCount = 0;
            int preNum = Integer.MIN_VALUE;
            while (cur != null || !stack.isEmpty()) {
                if (cur != null) {
                    stack.push(cur);
                    cur = cur.left;
                } else {
                    cur = stack.pop();
                    int num = cur.val;
                    if (num == preNum) {
                        curCount++;
                    } else {
                        if (curCount > maxCount){
                            maxCount = curCount;
                            res = new ArrayList<>();
                            res.add(preNum);
                        } else if (curCount == maxCount) {
                            res.add(preNum);
                        }
                        curCount = 1;
                    }
                    preNum = num;
                    cur = cur.right;
                }
            }
            if (curCount > maxCount){
                res = new ArrayList<>();
                res.add(preNum);
            } else if (curCount == maxCount) {
                res.add(preNum);
            }
            return  res.stream().mapToInt(Integer::intValue).toArray();
        }

    }

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
}
