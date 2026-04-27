package org.yg.algorithm.leetcode;

import java.util.Stack;

public class LeetCode150 {

    public static class Solution {
        public int evalRPN(String[] tokens) {
            Stack<Integer> stack = new Stack<>();
            for (String s : tokens) {
                try {
                    int num = Integer.parseInt(s);
                    stack.push(num);
                } catch (Exception e) {
                    int numAfter = stack.pop();
                    int numPre = stack.pop();
                    switch (s) {
                        case "+":
                            stack.push(numPre + numAfter);
                            break;
                        case "-":
                            stack.push(numPre - numAfter);
                            break;
                        case "*":
                            stack.push(numPre * numAfter);
                            break;
                        case "/":
                            stack.push(numPre / numAfter);
                            break;
                        default:
                            break;
                    }
                }
            }
            return stack.pop();
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.evalRPN(new String[]{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}));;
    }
}
