package org.yg.algorithm.leetcode;


import java.util.List;
import java.util.stream.Collectors;

public class LeetCode541 {

    public static class Solution {
        public String reverseStr(String s, int k) {
            if (s.length() == 1 || k == 1) {
                return s;
            }
            List<String> chars = s.chars().mapToObj(a -> String.valueOf((char) a)).collect(Collectors.toList());
            int left = 0;
            int right = 0;
            while (left < s.length()) {
                while (!(right == s.length() - 1 || right == left + k - 1)) {
                    right++;
                }

                swapSubString(chars, left, right);

                // update left,
                left = Math.min(s.length(), right + k + 1);
                right = left;
            }

            return String.join("", chars);
        }

        private void swapSubString(List<String> s, int left, int right) {
            while (left < right) {
                String tmp = s.get(left);
                s.set(left, s.get(right));
                s.set(right, tmp);
                left++;
                right--;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.reverseStr("abcd", 2));
    }

}