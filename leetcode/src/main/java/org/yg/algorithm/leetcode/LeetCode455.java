package org.yg.algorithm.leetcode;

import java.util.Arrays;

public class LeetCode455 {

    public static class Solution {
        public int findContentChildren(int[] g, int[] s) {
            Arrays.sort(g);
            Arrays.sort(s);
            int res = 0;
            int j = 0;
            for (int i = 0; i < s.length && j < g.length;) {
                if (s[i] >= g[j]) {
                    res++;
                    i++;
                    j++;
                } else {
                    i++;
                }
            }
            return res;
        }
    }

}
