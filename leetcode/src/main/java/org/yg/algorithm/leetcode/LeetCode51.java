package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCode51 {

    public static class Solution {

        private final List<List<String>> res = new ArrayList<>();
        private int[] cur;
        private int curOccupied = 0;
        private int diag1Occupied = 0;  // 新增：主对角线占用位集
        private int diag2Occupied = 0;  // 新增：副对角线占用位集
        private char[] chars;

        public List<List<String>> solveNQueens(int n) {
            cur = new int[n];
            Arrays.fill(cur, -1);
            chars = new char[n];
            Arrays.fill(chars, '.');
            doSolveNQueues(n, 0);
            return res;
        }

        private void doSolveNQueues(int n, int curRow) {
            if (curRow == n) {
                List<String> curRes = new ArrayList<>();
                for (int col : cur) {
                    chars[col] = 'Q';
                    curRes.add(new String(chars));
                    chars[col] = '.';
                }
                res.add(curRes);
                return;
            }

            for (int i = 0; i < n; ++i) {
                // 列冲突检查
                if (((curOccupied >> i) & 1) == 1) {
                    continue;
                }

                // ----- todo 开始：判断斜线是否被占据 -----
                // 主对角线标识: row - col，偏移 (n-1) 使其非负，范围 [0, 2n-2]
                int d1 = curRow - i + n - 1;
                // 副对角线标识: row + col，范围 [0, 2n-2]
                int d2 = curRow + i;
                // 如果任一斜线已被占用，则跳过该位置
                if (((diag1Occupied >> d1) & 1) == 1 || ((diag2Occupied >> d2) & 1) == 1) {
                    continue;
                }
                // ----- todo 结束 -----

                // 占据当前列和两条斜线
                curOccupied |= (1 << i);
                diag1Occupied |= (1 << d1);
                diag2Occupied |= (1 << d2);

                cur[curRow] = i;
                doSolveNQueues(n, curRow + 1);
                cur[curRow] = -1;

                // 恢复状态
                curOccupied &= ~(1 << i);
                diag1Occupied &= ~(1 << d1);
                diag2Occupied &= ~(1 << d2);
            }
        }
    }
    public static void main(String[] args) {
        Solution solution = new Solution();
    }

}
