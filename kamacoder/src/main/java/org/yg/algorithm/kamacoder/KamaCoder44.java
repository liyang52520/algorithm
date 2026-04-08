package org.yg.algorithm.kamacoder;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class KamaCoder44 {

    public static int minPart(int[][] nums) {
        int n = nums.length, m = nums[0].length;

        int[] prefixSum = new int[n];
        int[] suffixSum = new int[n];

        int[] colSum = new int[n];

        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = 0; j < m; j++) {
                sum += nums[i][j];
            }
            colSum[i] = sum;
        }
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += colSum[i];
            prefixSum[i] = sum;
        }

        sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            sum += colSum[i];
            suffixSum[i] = sum;
        }


        // compare prefix and suffix
        int minGap = Integer.MAX_VALUE;
        for (int i = 1; i < n; i++) {
            minGap = Math.min(minGap, Math.abs(prefixSum[i - 1] - suffixSum[i]));
        }
        return minGap;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] part = br.readLine().split(" ");
        int n = Integer.parseInt(part[0]), m = Integer.parseInt(part[1]);
        int[][] nums = new int[n][m];
        int[][] numsReverse = new int[m][n];

        for (int i = 0; i < n; i++) {
            part = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                int num = Integer.parseInt(part[j]);
                nums[i][j] = num;
                numsReverse[j][i] = num;
            }
        }

        System.out.println(Math.min(minPart(nums), minPart(numsReverse)));
    }

}
