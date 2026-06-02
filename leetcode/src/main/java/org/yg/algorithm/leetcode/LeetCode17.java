package org.yg.algorithm.leetcode;

import java.util.*;

public class LeetCode17 {

    public static class Solution {

        public List<String> letterCombinations(String digits) {
            Map<Character, List<String>> keyMap = new HashMap<>();
            keyMap.put('2', Arrays.asList("a", "b", "c"));
            keyMap.put('3', Arrays.asList("d", "e", "f"));
            keyMap.put('4', Arrays.asList("g", "h", "i"));
            keyMap.put('5', Arrays.asList("j", "k", "l"));
            keyMap.put('6', Arrays.asList("m", "n", "o"));
            keyMap.put('7', Arrays.asList("p", "q", "r", "s"));
            keyMap.put('8', Arrays.asList("t", "u", "v"));
            keyMap.put('9', Arrays.asList("w", "x", "y", "z"));
            List<String> res = new ArrayList<>();
            List<String> temp = new ArrayList<>();
            temp.add("");

            for (char c : digits.toCharArray()) {
                List<String> charList = keyMap.getOrDefault(c, new ArrayList<>());
                for (String tmpStr : temp) {
                    for (String charStr : charList) {
                        res.add(tmpStr + charStr);
                    }
                }
                temp = res;
                res = new ArrayList<>();
            }
            return temp;
        }
    }

}
