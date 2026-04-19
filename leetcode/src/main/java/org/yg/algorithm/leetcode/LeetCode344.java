package org.yg.algorithm.leetcode;


public class LeetCode344 {

    public static class Solution {
        public void reverseString(char[] s) {
            int left = 0, right = s.length -1;
            while (left < right) {
                char tmp = s[left];
                s[left] = s[right];
                s[right] = tmp;
                left++;
                right--;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
    }

}