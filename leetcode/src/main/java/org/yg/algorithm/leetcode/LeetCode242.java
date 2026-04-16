package org.yg.algorithm.leetcode;


public class LeetCode242 {

    public static class Solution {
        public boolean isAnagram(String s, String t) {
            if (s.length() != t.length()) {
                return false;
            }

            int[] sCount = new int[26];
            s.chars().forEach(i -> sCount[i - 97]++);
            int[] tCount = new int[26];
            t.chars().forEach(i -> tCount[i - 97]++);
            for (int i = 0; i < 26; i++) {
                if (sCount[i] != tCount[i]) {
                    return false;
                }
            }
            return true;
        }
    }

    public static void main(String[] args) {
    }

}