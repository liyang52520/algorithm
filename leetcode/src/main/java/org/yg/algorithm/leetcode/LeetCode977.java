package org.yg.algorithm.leetcode;


import java.util.Arrays;

public class LeetCode977 {

    public static class Solution {
        public int[] sortedSquares(int[] nums) {
            int n = nums.length;
            int[] res = new int[n];
            int left = 0, right = n - 1;
            int resIdx = n - 1;

            while (resIdx >= 0) {
                if (-nums[left] > nums[right]) {
                    res[resIdx] = nums[left] * nums[left];
                    left++;
                } else {
                    res[resIdx] = nums[right] * nums[right];
                    right--;
                }

                resIdx--;
            }

            return res;
        }
    }

    public static void main(String[] args) {

        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.sortedSquares(new int[]{-7, -3})));

    }

}