package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCode18 {

    public static class Solution {

        public List<List<Integer>> fourSum(int[] nums, int target) {
            Arrays.sort(nums);
            int n = nums.length;
            List<List<Integer>> result = new ArrayList<>();
            for (int i = 0; i < n - 3; i++) {
                // 去重复
                if (i > 0 && nums[i] == nums[i - 1]) {
                    continue;
                }
                if (nums[i] > 0 && nums[i] > target) {
                    continue;
                }
                for (int j = i + 1; j < n - 2; j++) {
                    if (j > i + 1 && nums[j] == nums[j - 1]) {
                        continue;
                    }
                    if (nums[i] + nums[j] > 0 && nums[i] + nums[j] > target) {
                        continue;
                    }
                    int left = j + 1;
                    int right = n - 1;
                    while (left < right) {
                        int sum = nums[i] + nums[j] + nums[left] + nums[right];
                        if (sum == target) {
                            result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                            while (left < right && nums[left] == nums[left + 1]) left++;
                            while (left < right && nums[right] == nums[right - 1]) right--;
                            left++;
                            right--;
                        } else if (sum < target) {
                            left++;
                        } else {
                            right--;
                        }
                    }
                }
            }
            return result;
        }

        public static void main(String[] args) {
            Solution s = new Solution();
            List<List<Integer>> result = s.fourSum(new int[]{1, -2, -5, -4, -3, 3, 3, 5}, -11);
            for (List<Integer> sR : result) {
                System.out.println(sR);
            }
        }

    }
}
