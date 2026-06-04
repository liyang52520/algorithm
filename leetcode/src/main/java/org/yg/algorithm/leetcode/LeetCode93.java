package org.yg.algorithm.leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class LeetCode93 {

    public static class Solution {

        List<String> res = new ArrayList<>();

        List<String> cur = new ArrayList<>();

        public List<String> restoreIpAddresses(String s) {
            if (s.length() < 4) {
                return Collections.emptyList();
            }

            doRestoreIpAddress(s, 0);
            return res;
        }

        private void doRestoreIpAddress(String s, int start) {
            if (cur.size() == 4 && start == s.length()) {
                res.add(String.join(".", cur));
                return;
            }
            // 不可能成功了
            if (cur.size() == 4 && start < s.length()) {
                return;
            }

            int maxValue = s.length() - (3 - cur.size());
            for (int i = start; i < maxValue; i++) {
                String subString = s.substring(start, i + 1);
                if (checkValid(subString)) {
                    cur.add(subString);
                    doRestoreIpAddress(s, i + 1);
                    cur.remove(cur.size() - 1);
                }
            }
        }

        private boolean checkValid(String s) {
            if (s.length() == 1) {
                return true;
            }
            if (s.length() > 3) {
                return false;
            }
            if (s.length() > 1 && s.charAt(0) == '0') {
                return false;
            }
            return Integer.parseInt(s) <= 255;
        }

    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.restoreIpAddresses("25525511135"));
    }

}
