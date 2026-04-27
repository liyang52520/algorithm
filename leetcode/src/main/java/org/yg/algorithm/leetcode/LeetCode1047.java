package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class LeetCode1047 {

    public static class Solution {
        public String removeDuplicates(String s) {
            List<Character> characterList = new ArrayList<>();

            for (char c : s.toCharArray()) {
                if (characterList.isEmpty() || c != characterList.get(characterList.size() - 1)) {
                    characterList.add(c);
                    continue;
                }

                // not empty
                characterList.remove(characterList.size() - 1);
            }

            return characterList.stream().map(String::valueOf).collect(Collectors.joining(""));
        }

        public static void main(String[] args) {
        }
    }
}
