package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class LeetCode90 {

    public static class Solution {

        List<List<Integer>> result = new ArrayList<>();// 存放符合条件结果的集合
        List<Integer> path = new ArrayList<>();// 用来存放符合条件结果

        public List<List<Integer>> subsetsWithDup(int[] nums) {
            Arrays.sort(nums);
            subsetsHelper(nums, 0);
            return result;
        }

        private void subsetsHelper(int[] nums, int startIndex) {
            result.add(new ArrayList<>(path));//「遍历这个树的时候，把所有节点都记录下来，就是要求的子集集合」。
            if (startIndex >= nums.length) { //终止条件可不加
                return;
            }
            for (int i = startIndex; i < nums.length; i++) {
                if (i > startIndex && nums[i] == nums[i - 1]) {
                    continue;
                }
                path.add(nums[i]);
                subsetsHelper(nums, i + 1);
                path.remove(path.size() - 1);
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.subsetsWithDup(new int[]{4,4,4,1,4}));
    }

}
