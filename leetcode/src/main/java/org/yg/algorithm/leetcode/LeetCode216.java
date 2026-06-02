package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class LeetCode216 {

    public static class Solution {

        private final List<List<Integer>> res = new ArrayList<>();

        private final List<Integer> cur = new ArrayList<>();

        public List<List<Integer>> combinationSum3(int k, int n) {
            // k 个数的极限条件，先判断是否可行了
            int maxValue = 9 * k - k * (k - 1) / 2;
            if (n > maxValue) {
                return Collections.emptyList();
            }

            doCombineSum3(1, k, n);

            return res;
        }

        public void doCombineSum3(int start, int k, int n) {
            if (n < 0) {
                return;
            }
            if (k == 0 && n == 0) {
                res.add(new ArrayList<>(cur));
            }

            for (int i = start; i <= 9; i++) {
                cur.add(i);

                doCombineSum3(i + 1, k - 1, n - i);

                cur.remove(cur.size() - 1);
            }
        }
    }
}
