package org.yg.algorithm.leetcode;


public class LeetCode704 {

    public static class Solution {
        public int search(int[] nums, int target) {
            // nums 为升序数组（数量大于1），并且所有元素是不重复的
            int left = 0, right = nums.length - 1;
            while (left <= right) {
                int mid = (left + right) >> 1;
                int num = nums[mid];
                if (num == target) {
                    return mid;
                } else if (num > target) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            return -1;
        }
    }

    public static void main(String[] args) {
    }
}