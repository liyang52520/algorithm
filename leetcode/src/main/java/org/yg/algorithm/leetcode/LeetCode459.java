package org.yg.algorithm.leetcode;

import java.util.Arrays;

public class LeetCode459 {

    public static class Solution {

        public boolean repeatedSubstringPattern(String s) {
            int[] commonArray = getCommonPreAndSuffixArray(s);

            System.out.println(Arrays.toString(commonArray));

            int n = s.length();
            int maxCommon = commonArray[n];

            int k = n - maxCommon;
            return n != k && n % k == 0;
        }

        public int[] getCommonPreAndSuffixArray(String s) {
            if (s == null || s.isEmpty()) {
                return new int[0];
            }

            int n = s.length();
            int[] lenArray = new int[n + 1];
            lenArray[0] = -1;
            lenArray[1] = 0;

            for (int i = 2; i <= n; i++) {
                int len = lenArray[i - 1];
                while (len >= 0 && s.charAt(len) != s.charAt(i - 1)) {
                    len = lenArray[len];
                }
                lenArray[i] = len + 1;
            }

            return lenArray;
        }

        public static void main(String[] args) {
            Solution s = new Solution();
            System.out.println(s.repeatedSubstringPattern("abac"));
        }

    }
}
