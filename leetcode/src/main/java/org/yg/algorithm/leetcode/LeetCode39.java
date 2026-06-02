package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode39 {

    public static class Solution {

        private final List<List<Integer>> res = new ArrayList<>();

        private final List<Integer> tmpList = new ArrayList<>();

        public List<List<Integer>> combinationSum(int[] candidates, int target) {
            dfs(candidates, 0, target);
            return res;
        }

        private void dfs(int[] candidates, int startIdx, int target) {
            if (target == 0) {
                res.add(new ArrayList<>(tmpList));
                return;
            }
            if (target < 1) {
                return;
            }

            for (int i = startIdx; i < candidates.length; i++) {
                tmpList.add(candidates[i]);
                dfs(candidates, i, target - candidates[i]);
                tmpList.remove(tmpList.size() - 1);
            }

        }

    }

}
