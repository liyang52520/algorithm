package org.yg.algorithm.leetcode;

import java.util.Stack;

public class LeetCode20 {

    public static class Solution {
        public boolean isValid(String s) {
            Stack<Character> characterStack = new Stack<>();
            for (Character c: s.toCharArray()) {
                if (c == '(' || c == '[' || c== '{') {
                    characterStack.push(c);
                } else {
                    if (characterStack.isEmpty()) {
                        return false;
                    }
                    char preC = characterStack.pop();
                    if ( c == ')') {
                        if (preC != '(') {
                            return false;
                        }
                    } else if (c == ']') {
                        if (preC != '[') {
                            return false;
                        }
                    } else {
                        if (preC != '{') {
                            return false;
                        }
                    }
                }
            }
            return characterStack.isEmpty();
        }

        public static void main(String[] args) {
        }

    }
}
