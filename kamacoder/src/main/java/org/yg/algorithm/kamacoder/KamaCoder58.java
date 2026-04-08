package org.yg.algorithm.kamacoder;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class KamaCoder58 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];
        int[] preSum = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(br.readLine());
            sum += nums[i];
            preSum[i] = sum;
        }

        String line;
        while ((line = br.readLine()) != null) {
            String[] idxes = line.split(" ");
            int left = Integer.parseInt(idxes[0]);
            int right = Integer.parseInt(idxes[1]);
            if (left == 0) {
                System.out.println(preSum[right]);
            } else {
                System.out.println(preSum[right] - preSum[left - 1]);
            }
        }
    }

}
