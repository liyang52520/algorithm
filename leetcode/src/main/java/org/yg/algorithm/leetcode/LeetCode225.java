package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.List;

public class LeetCode225 {

    public static class MyStack {

        private final List<Integer> numList = new ArrayList<>();

        public MyStack() {
        }

        public void push(int x) {
            numList.add(x);
        }

        public int pop() {
            int n = numList.get(numList.size() - 1);
            numList.remove(numList.size() - 1);
            return n;
        }

        public int top() {
            return numList.get(numList.size() - 1);
        }

        public boolean empty() {
            return numList.isEmpty();
        }
    }

    public static class Solution {
        public static void main(String[] args) {
        }
    }
}
