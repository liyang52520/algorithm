package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode46 {

    public static class Solution {

        private final List<List<Integer>> res = new ArrayList<>();

        private final List<Integer> cur = new ArrayList<>();

        public List<List<Integer>> permute(int[] nums) {
            doPermute(nums, 0);
            return res;
        }

        private void doPermute(int[] nums, int startIndex) {
            if (startIndex == nums.length) {
                res.add(new ArrayList<>(cur));
            }


            for (int i = startIndex; i < nums.length; i++) {
                swap(nums, startIndex, i);
                cur.add(nums[startIndex]);
                doPermute(nums, startIndex + 1);
                cur.remove(cur.size() - 1);
                swap(nums, startIndex, i);
            }

        }

        private void swap(int[] nums, int idx1, int idx2) {
            int temp = nums[idx1];
            nums[idx1] = nums[idx2];
            nums[idx2] = temp;
        }


    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.permute(new int[]{1, 2, 3}));
    }

}
