package org.yg.algorithm.kamacoder;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class KamaCoder55 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        String inputS = br.readLine();
        int n = inputS.length();
        if (k >= n) {
            System.out.println(inputS);
        }
        String preS = inputS.substring(0, n - k);
        String backS = inputS.substring(n - k, n);
        System.out.println(backS + preS);
    }

}
