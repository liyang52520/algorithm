package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class LeetCode37 {

    public static class Solution {

        private final List<Set<Character>> rowSets = new ArrayList<>(9);
        private final List<Set<Character>> colSets = new ArrayList<>(9);
        private final List<Set<Character>> blockSets = new ArrayList<>(9);
        private final char[] nums = new char[]{'1', '2', '3', '4', '5', '6', '7', '8', '9'};

        public void solveSudoku(char[][] board) {
            // init
            for (int i = 0; i < 9; i++) {
                rowSets.add(new HashSet<>(9));
                colSets.add(new HashSet<>(9));
                blockSets.add(new HashSet<>(9));
            }
            for (int row = 0; row < 9; row++) {
                for (int col = 0; col < 9; col++) {
                    char c = board[row][col];
                    if ('.' != c) {
                        rowSets.get(row).add(c);
                        colSets.get(col).add(c);
                        int tmpRow = row / 3;
                        int tmpCol = col / 3;
                        blockSets.get(tmpRow * 3 + tmpCol).add(c);
                    }
                }
            }
            doSolveSudoku(board, 0, 0);
        }

        private boolean doSolveSudoku(char[][] board, int row, int col) {
            if (row == 9) {
                return true;
            }
            int nextRow = row;
            int nextCol = col + 1;
            if (nextCol == 9) {
                nextCol = 0;
                nextRow++;
            }
            if (board[row][col] != '.') {
                return doSolveSudoku(board, nextRow, nextCol);
            }

            Set<Character> rowSet = rowSets.get(row);
            Set<Character> colSet = colSets.get(col);
            int tmpRow = row / 3;
            int tmpCol = col / 3;
            Set<Character> blockSet = blockSets.get(tmpRow * 3 + tmpCol);


            for (char num : nums) {
                // 判断是否重复
                if (rowSet.contains(num)) {
                    continue;
                }
                if (colSet.contains(num)) {
                    continue;
                }
                if (blockSet.contains(num)) {
                    continue;
                }

                board[row][col] = num;
                rowSet.add(num);
                colSet.add(num);
                blockSet.add(num);

                if (doSolveSudoku(board, nextRow, nextCol)) {
                    return true;
                }

                board[row][col] = '.';
                rowSet.remove(num);
                colSet.remove(num);
                blockSet.remove(num);
            }
            return false;
        }

    }

}
