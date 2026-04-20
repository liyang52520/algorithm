package org.yg.algorithm.leetcode;

public class LeetCode28 {

    public static class Solution {

        public int strStr(String haystack, String needle) {
            // 先去除最基本的边界情况
            if (haystack == null || haystack.isEmpty()
                    || needle == null || needle.isEmpty()
                    || haystack.length() < needle.length()) {
                return -1;
            }

            // 计算得到 next 数组
            int[] next = getCommonPreAndSuffixArray(needle);

            int n = haystack.length(), m = needle.length();
            int i = 0, j = 0;
            while (i < n && j < m) {
                if (j == -1 || haystack.charAt(i) == needle.charAt(j)) {
                    i++;
                    j++;
                } else {
                    // 未匹配上，回滚 j 到已匹配的字符串 needle[0:j]
                    j = next[j];
                }

            }

            return j == m ? i - m : -1;
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
                while (len > 0 && s.charAt(len) != s.charAt(i - 1)) {
                    len = lenArray[len];
                }
                if (s.charAt(len) == s.charAt(i - 1)) {
                    lenArray[i] = len + 1;
                } else {
                    lenArray[i] = 0;                     // len == 0 且字符不等
                }
            }

            return lenArray;
        }

    }
}
