// https://www.geeksforgeeks.org/problems/find-pair-given-difference1559/1

// POTD 17.05.24

// Find Pair Given Difference

// Given an array arr[] of size n and an integer x, return 1 if there exists a pair of elements in the array whose absolute difference is x, otherwise, return -1.

// Example 1:

// Input:
// n = 6
// x = 78
// arr[] = {5, 20, 3, 2, 5, 80}
// Output:
// 1
// Explanation:
// Pair (2, 80) have absolute difference of 78.
// Example 2:

// Input:
// n = 5
// x = 45
// arr[] = {90, 70, 20, 80, 50}
// Output:
// -1
// Explanation:
// There is no pair with absolute difference of 45.
// Your Task:
// You need not take input or print anything. Your task is to complete the function findPair() which takes integers n, x, and an array arr[] as input parameters and returns 1 if the required pair exists, return -1 otherwise.

// Expected Time Complexity: O(n* Log(n)).
// Expected Auxiliary Space: O(1).

import java.io.*;
import java.util.*;

class IntArray {
    public static int[] input(BufferedReader br, int n) throws IOException {
        String[] s = br.readLine().trim().split(" ");
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
            a[i] = Integer.parseInt(s[i]);

        return a;
    }

    public static void print(int[] a) {
        for (int e : a)
            System.out.print(e + " ");
        System.out.println();
    }

    public static void print(ArrayList<Integer> a) {
        for (int e : a)
            System.out.print(e + " ");
        System.out.println();
    }
}

public class FindPairGivenDifference {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n;
        n = Integer.parseInt(br.readLine());

        int x;
        x = Integer.parseInt(br.readLine());

        int[] arr = IntArray.input(br, n);

        Solution obj = new Solution();
        int res = obj.findPair(n, x, arr);

        System.out.println(res);

        br.close();
    }
}

class Solution {
    public int findPair(int n, int x, int[] arr) {
        // code here
        Arrays.sort(arr);

        int beg, end, mid, item;

        for (int i = 0; i < n; i++) {
            item = arr[i] + x;

            beg = i + 1;
            end = n - 1;

            while (beg <= end) {
                mid = (beg + end) / 2;
                if (arr[mid] == item) {
                    return 1;
                } else if (item > arr[mid]) {
                    beg = mid + 1;
                } else if (item < arr[mid]) {
                    end = mid - 1;
                }
            }
        }
        return -1;
    }
}