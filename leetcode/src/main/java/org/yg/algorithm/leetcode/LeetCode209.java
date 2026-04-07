package org.yg.algorithm.leetcode;


import java.util.Arrays;

public class LeetCode209 {

    public static class Solution {
        public int minSubArrayLen(int target, int[] nums) {
            // 子数组是连续的
            int n = nums.length;
            int left = 0, right = 0;
            int sum = 0;
            int minCount = n + 1;
            while (right < n) {
                sum += nums[right];

                while (sum >= target) {
                    minCount = Math.min(minCount, right - left + 1);
                    sum -= nums[left];
                    left++;
                }
                right++;
            }

            if (minCount == n + 1) {
                return 0;
            }
            return minCount;
        }

        /**
         * 返回能够组成 target 的最少元素个数，每个元素最多使用一次。
         * 如果无法组成 target，则返回 0。
         *
         * @param nums   正整数数组，元素范围 (0, 10000)
         * @param target 目标和，范围 [0, 1000000)
         * @return 最少元素个数，若不能组成则返回 0
         */
        public int minElements(int[] nums, int target) {
            if (target == 0) {
                return 0;
            }

            // 过滤掉大于 target 的元素（它们不可能被选）
            int[] filtered = Arrays.stream(nums).filter(n -> n <= target).toArray();

            // 如果某个元素恰好等于 target，直接返回 1
            for (int num : filtered) {
                if (num == target) {
                    return 1;
                }
            }

            // 0-1 背包 DP，dp[i] 表示组成 i 所需的最少元素个数
            int INF = Integer.MAX_VALUE / 2; // 防止溢出
            int[] dp = new int[target + 1];
            Arrays.fill(dp, INF);
            dp[0] = 0;

            for (int num : filtered) {
                // 倒序更新，保证每个元素只用一次
                for (int i = target; i >= num; i--) {
                    if (dp[i - num] != INF) {
                        dp[i] = Math.min(dp[i], dp[i - num] + 1);
                    }
                }
                System.out.println(Arrays.toString(dp));
            }

            return dp[target] == INF ? 0 : dp[target];
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
//        System.out.println(solution.minSubArrayLen(11, new int[]{1, 2, 3, 4, 5}));
        System.out.println(solution.minElements( new int[]{1, 1, 3, 3, 4}, 6));
    }

}