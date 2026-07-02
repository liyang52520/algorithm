package org.yg.algorithm.leetcode;

public class LeetCode376 {

    public static class Solution {

        public int wiggleMaxLength(int[] nums) {
            // 其实并不难，其实很简单
            // 计算一下波峰和波谷的数量就可以了
            int n = nums.length;
            if (n < 2) {
                return n;
            }
            int prevdiff = nums[1] - nums[0];
            int ret = prevdiff != 0 ? 2 : 1;
            for (int i = 2; i < n; i++) {
                int diff = nums[i] - nums[i - 1];
                // 处理平坡问题
                if ((diff > 0 && prevdiff <= 0) || (diff < 0 && prevdiff >= 0)) {
                    ret++;
                    prevdiff = diff;
                }
            }
            return ret;
        }

        public static void main(String[] args) {
        }
    }
}
