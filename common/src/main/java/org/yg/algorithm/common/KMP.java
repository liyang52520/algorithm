package org.yg.algorithm.common;

import java.util.Arrays;

public class KMP {

    /**
     * 寻找 pattern 字符串在 s 中出现的索引
     *
     * @param s       源字符串
     * @param p 目标字符串（模式）
     * @return 索引位置，如果未找到返回 -1
     */
    public static int indexOf(String s, String p) {
        // 先去除最基本的边界情况
        if (s == null || s.isEmpty() || p == null || p.isEmpty() || s.length() < p.length()) {
            return -1;
        }

        // 计算得到 next 数组
        int[] next = getNextArrayForKMP(p);

        System.out.println(Arrays.toString(next));

        // 基于 next 数组进行匹配
        int n = s.length(), m = p.length();
//        int i = 0, j = 0;
//        while (i < n && j < m) {
//            if (j == -1 || s.charAt(i) == pattern.charAt(j)) {
//                // 相等则继续匹配
//                i++;
//                j++;
//            } else {
//                // 不相等，就回滚已匹配部分，怎么回滚，已经匹配了索引 j-1 的部分
//                j = next[j];
//            }
//        }
//
//        // 基于 next 数组进行匹配
//        return j == m ? i - j : -1;

        // j 代表已经匹配的长度
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j != -1 && s.charAt(i) != p.charAt(j)) {
                j = next[j];
            }
            if (j == -1 || s.charAt(i) == p.charAt(j)) {
                j++;
            }
            if (j == m) {
                return i - m + 1;
            }
        }
        return -1;
    }

    /**
     * 计算用于 kmp 算法的 next 数组
     * next[i] 代表字符串 s 子串 模式串前 i 个字符组成的子串中，最长的相等真前缀和真后缀的长度
     * 最大公共前后缀：ABCAB 的最大公共前后缀就是 AB
     *
     * @param s
     * @return
     */
    public static int[] getNextArrayForKMP(String s) {
        if (s == null || s.isEmpty()) {
            return new int[0];
        }

        int n = s.length();
        int[] next = new int[n + 1];
        next[0] = -1;
        next[1] = 0;

        for (int i = 2; i <= n; i++) {           // i 表示前 i 个字符
            int len = next[i - 1];               // 前 i-1 个字符的最长相等前后缀长度
            while (len > 0 && s.charAt(len) != s.charAt(i - 1)) {
                len = next[len];
            }
            if (s.charAt(len) == s.charAt(i - 1)) {
                next[i] = len + 1;
            } else {
                next[i] = 0;                     // len == 0 且字符不等
            }
        }
        return next;
    }

    public static void main(String[] args) {
        System.out.println(indexOf("BBC ABCDAB ABCDABCDABDE", "ABCDABD"));
        ;
    }

}