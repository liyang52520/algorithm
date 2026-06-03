package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode131 {

    public static class Solution {
        private final List<List<String>> res = new ArrayList<>();

        private final List<String> curRes = new ArrayList<>();

        public List<List<String>> partition(String s) {
            // 假设我已经有一个 dp[i][j] 代表 [i,j] 子串是否是回文子串
            int n = s.length();
            boolean[][] dp = new boolean[n][n];

            for (int stepSize = 1; stepSize <= n; stepSize++) {
                for (int i = 0; i <= n - stepSize; i++) {
                    if (stepSize == 1) {
                        dp[i][i] = true;
                    } else if (stepSize == 2) {
                        dp[i][i + 1] = s.charAt(i) == s.charAt(i + 1);
                    } else {
                        dp[i][i + stepSize - 1] = dp[i + 1][i + stepSize - 2] && s.charAt(i) == s.charAt(i + stepSize - 1);
                    }
                }
            }

            // 然后呢？怎么优雅的拆分子问题
            doPartition(0, s, dp);
            return res;
        }

        private void doPartition(int startIdx, String s, boolean[][] dp) {
            // 结束条件
            if (startIdx == s.length()) {
                res.add(new ArrayList<>(curRes));
            }

            for (int i = startIdx; i < s.length(); i++) {
                if (dp[startIdx][i]) {
                    curRes.add(s.substring(startIdx, i + 1));
                    doPartition(i + 1, s, dp);
                    curRes.remove(curRes.size() - 1);
                }
            }
        }

    }
}
