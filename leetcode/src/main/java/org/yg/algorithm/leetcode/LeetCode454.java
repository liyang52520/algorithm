package org.yg.algorithm.leetcode;

import java.util.HashMap;
import java.util.Map;

public class LeetCode454 {

    public static class Solution {
        public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
            Map<Long, Integer> preCount = countSum(nums1, nums2);
            Map<Long, Integer> befCount = countSum(nums3, nums4);

            int res = 0;
            for (Map.Entry<Long, Integer> e : preCount.entrySet()) {
                long num = e.getKey();
                if (befCount.containsKey(-num)) {
                    res += e.getValue() * befCount.get(-num);
                }
            }

            return res;
        }

        private Map<Long, Integer> countSum(int[] nums1, int[] nums2) {
            Map<Long, Integer> count = new HashMap<>();
            for (int num1 : nums1) {
                for (int num2 : nums2) {
                    long sum = (long) num1 + (long) num2;
                    if (!count.containsKey(sum)) {
                        count.put(sum, 1);
                    } else {
                        count.put(sum, count.get(sum) + 1);
                    }
                }
            }
            return count;
        }

        public static void main(String[] args) {
        }
    }
}
