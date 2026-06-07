package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class LeetCode491 {

    public static class Solution {

        private final List<List<Integer>> res = new ArrayList<>();

        private final List<Integer> cur = new ArrayList<>();

        public List<List<Integer>> findSubsequences(int[] nums) {
            doFindSubsequences(nums, 0);
            return res;
        }

        private void doFindSubsequences(int[] nums, int startIndex) {
            if (cur.size() > 1) {
                res.add(new ArrayList<>(cur));
            }
            if (startIndex == nums.length) {
                return;
            }

            Set< Integer> scannedNum = new HashSet<>();
            for (int i = startIndex; i < nums.length; i++) {
                if (scannedNum.contains(nums[i])) {
                    continue;
                }
                scannedNum.add(nums[i]);
                if (cur.isEmpty() || cur.get(cur.size() - 1) <= nums[i]) {
                    cur.add(nums[i]);
                    doFindSubsequences(nums, i + 1);
                    cur.remove(cur.size() - 1);
                }
            }

        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.findSubsequences(new int[]{4, 4, 3, 2, 1}));
    }

}
