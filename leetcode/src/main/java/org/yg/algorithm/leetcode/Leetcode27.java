package org.yg.algorithm.leetcode;

import java.util.Arrays;

public class Leetcode27 {

    public static class Solution {
        public int removeElement(int[] nums, int val) {
            int left = 0;
            int right = nums.length;
            while (left < right) {
                if (nums[left] == val) {
                    nums[left] = nums[right - 1];
                    right--;
                } else {
                    left++;
                }
            }
            return left;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = new int[] {0,1,2,2,3,0,4,2};
        solution.removeElement(nums, 2);
        System.out.println("nums = " + Arrays.toString(nums));

    }

}
