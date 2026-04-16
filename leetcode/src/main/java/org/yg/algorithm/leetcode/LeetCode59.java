package org.yg.algorithm.leetcode;

import java.util.Arrays;

public class LeetCode59 {

    public static class Solution {
        public int[][] generateMatrix(int n) {
            int[][] res = new int[n][n];
            int left = 0, right = n - 1, top = 0, bottom = n - 1;

            int num = 1;
            while (left <= right && top <= bottom) {
                // ->
                for (int i = left; i <= right; i++) {
                    res[top][i] = num;
                    num++;
                }

                // down
                for (int i = top + 1; i <= bottom; i++) {
                    res[i][right] = num;
                    num++;
                }

                // <-
                for (int i = right - 1; i >= left; i--) {
                    res[bottom][i] = num;
                    num++;
                }

                // up
                for (int i = bottom - 1; i > top; i--) {
                    res[i][left] = num;
                    num++;
                }

                left++;
                right--;
                top++;
                bottom--;
            }
            return res;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 3;
        int[][] res = solution.generateMatrix(n);
        for (int i = 0; i < n; i++) {
            System.out.println(Arrays.toString(res[i]));
        }
    }

}
