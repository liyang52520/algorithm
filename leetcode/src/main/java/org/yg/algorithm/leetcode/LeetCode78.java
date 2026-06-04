package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode78 {

    public static class Solution {

        List<List<Integer>> res = new ArrayList<>();

        List<Integer> cur = new ArrayList<>();

        public List<List<Integer>> subsets(int[] nums) {
            doSubsets(nums, 0);
            return res;
        }

        private void doSubsets(int[] nums, int startIndex) {
            if (startIndex == nums.length) {
                res.add(new ArrayList<>(cur));
                return;
            }

            doSubsets(nums, startIndex + 1);
            cur.add(nums[startIndex]);
            doSubsets(nums, startIndex + 1);
            cur.remove(cur.size() - 1);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.subsets(new int[]{1, 2, 3}));
    }

}
