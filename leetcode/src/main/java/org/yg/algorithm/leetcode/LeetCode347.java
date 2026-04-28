package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LeetCode347 {

    public static class Solution {

        public static int[] topKFrequent(int[] nums, int k) {
            // 1. 统计每个数字出现的频率
            Map<Integer, Integer> freqMap = new HashMap<>();
            for (int num : nums) {
                freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
            }

            // 2. 创建桶数组，下标表示频率，值存储拥有该频率的元素列表
            List<Integer>[] bucket = new List[nums.length + 1];
            for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
                int freq = entry.getValue();
                if (bucket[freq] == null) {
                    bucket[freq] = new ArrayList<>();
                }
                bucket[freq].add(entry.getKey());
            }

            // 3. 从高频率往低频率遍历桶，收集结果
            int[] result = new int[k];
            int index = 0;
            for (int i = bucket.length - 1; i >= 0 && index < k; i--) {
                if (bucket[i] != null) {
                    for (int num : bucket[i]) {
                        result[index++] = num;
                        if (index == k) {
                            return result;
                        }
                    }
                }
            }
            return result;
        }

        public static void main(String[] args) {
            Solution solution = new Solution();
            solution.topKFrequent(new int[]{1, 1, 1, 2, 2, 3}, 2);
        }

    }
}
