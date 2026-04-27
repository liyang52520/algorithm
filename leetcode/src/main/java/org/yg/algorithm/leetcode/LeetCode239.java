package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCode239 {

    public static class Solution {


        public int[] maxSlidingWindow(int[] nums, int k) {

            int[] res = new int[nums.length - k + 1];

            List<Integer> nodeList = new ArrayList<>();
            for (int i = 0; i < k; i++) {
                refreshWindow(nodeList, i, nums[i], k, nums);
            }
            res[0] = nodeList.get(0);

            for (int i = k; i < nums.length; i++) {
                refreshWindow(nodeList, i, nums[i], k, nums);
                res[i - k + 1] = nodeList.get(0);
            }

            return res;
        }

        public void refreshWindow(List<Integer> nodeList, int index, int value, int k, int[] nums) {
            while (!nodeList.isEmpty() && nodeList.get(nodeList.size() - 1) < value) {
                nodeList.remove(nodeList.size() - 1);
            }
            nodeList.add(nodeList.size(), value);
            // 从头删除数据
            int j = index - k;
            if (j < 0) {
                return;
            }
            int num = nums[j];
            if (num == nodeList.get(0)) {
                nodeList.remove(0);
            }

        }

        public static void main(String[] args) {
            Solution solution = new Solution();
            System.out.println(Arrays.toString(solution.maxSlidingWindow(new int[]{1, 3, -1, -3, 5, 3, 6, 7}, 3)));
        }

    }
}
