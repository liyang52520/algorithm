package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class LeetCode77 {

    public static class Solution {
        public List<List<Integer>> combine(int n, int k) {
            return combineHelper(1, n, k);
        }

        public List<List<Integer>> combineHelper(int low, int high, int k) {
            // 保证范围合理
            if (low > high) {
                return Collections.emptyList();
            }
            if (high - low + 1 < k) {
                return Collections.emptyList();
            }
            if (high - low + 1 == k) {
                return Collections.singletonList(IntStream.rangeClosed(low, high).boxed().collect(Collectors.toList()));
            }
            if (k == 1) {
                return IntStream.rangeClosed(low, high).boxed().map(Collections::singletonList).collect(Collectors.toList());
            }

            // 现在的范围是合理的
            List<List<Integer>> res = new ArrayList<>();
            for (int i = low; i < high; i++) {
                List<List<Integer>> subRes = combineHelper(i + 1, high, k - 1);
                if (!subRes.isEmpty()) {
                    for (List<Integer> list : subRes) {
                        List<Integer> newList = new ArrayList<>();
                        newList.add(i);
                        newList.addAll(list);
                        res.add(newList);
                    }
                }
            }
            return res;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.combine(4, 2));
    }
}
