package org.yg.algorithm.leetcode;

import java.util.Stack;

public class LeetCode513 {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static class Solution {

        public int findBottomLeftValue(TreeNode root) {

            Stack<TreeNode> st = new Stack<>();
            int maxDepth = 0;
            int depth = 0;
            int res = root.val;
            st.push(root);
            while (!st.empty()) {
                TreeNode node = st.peek();
                if (node != null) {
                    st.pop(); // 将该节点弹出，避免重复操作，下面再将中右左节点添加到栈中（后序遍历-左右中，入栈顺序中右左）
                    st.push(node);                          // 添加中节点
                    st.push(null); // 中节点访问过，但是还没有处理，加入空节点做为标记。
                    if (node.right != null) {
                        st.push(node.right);  // 添加右节点（空节点不入栈）
                    }
                    if (node.left != null) {
                        st.push(node.left);
                    }    // 添加左节点（空节点不入栈）
                    depth++;
                    if (node.left != null && depth > maxDepth) {
                        maxDepth = depth;
                        res = node.left.val;
                    }
                    if (node.left == null && node.right != null && depth > maxDepth) {
                        maxDepth = depth;
                        res = node.right.val;
                    }
                } else { // 只有遇到空节点的时候，才将下一个节点放进结果集
                    st.pop();           // 将空节点弹出
                    node = st.peek();    // 重新取出栈中元素
                    st.pop();
                    depth--;
                }

            }
            return res;
        }

    }
}
