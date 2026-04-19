package org.yg.algorithm.kamacoder;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class KamaCoder54 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputS = br.readLine();
        StringBuilder sb = new StringBuilder();
        for (char c : inputS.toCharArray()) {
            if (Character.isDigit(c)) {
                sb.append("number");
            } else {
                sb.append(c);
            }
        }
        System.out.println(sb);
    }

}
