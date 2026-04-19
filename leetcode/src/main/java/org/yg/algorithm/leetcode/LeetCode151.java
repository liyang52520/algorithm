package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode151 {

    public static class Solution {

        public String reverseWords(String s) {
            List<String> words = new ArrayList<>();
            for (String word: s.split(" ")) {
                if (word.isEmpty()) {
                    continue;
                }

                if (word.charAt(0) == ' '){
                    continue;
                }

                words.add(word);
            }

            if (words.isEmpty()) {
                return "";
            }

            int left = 0, right = words.size() - 1;
            while (left < right) {
                String tmp = words.get(left);
                words.set(left, words.get(right));
                words.set(right, tmp);
                left++;
                right--;
            }
            return String.join(" ", words);
        }

        public static void main(String[] args) {
        }

    }
}
