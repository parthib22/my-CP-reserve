// https://www.geeksforgeeks.org/problems/find-the-closest-number5513/1

// POTD 19.05.24

// Find the closest number

// Given a sorted array arr[] of positive integers. The task is to find the closest value in the array to the given number k. The array may contain duplicate values.

// Note: If the difference with k is the same for two values in the array return the greater value.

// Example 1:
// Input: 
// n = 4
// k = 4
// arr[] = {1, 3, 6, 7}
// Output: 
// 3
// Explanation:
// We have array arr={1, 3, 6, 7} and target is 4. If we look at the absolute difference of target with every element of the array we will get { |1-4|, |3-4|, |6-4|, |7-4| }  = {3, 1, 2, 3}. So, the closest number is 3.

// Example 2:
// Input:
// n = 7
// k = 4
// arr[] = {1, 2, 3, 5, 6, 8, 9}
// Output:
// 5
// Explanation:
// The absolute difference of 4 is 1 from both 3 and 5. According to the question, we have to return greater value, which is 5.
// Your Task:
// This is a function problem. The input is already taken care of by the driver code. You only need to complete the function findClosest() that takes integers n and k and sorted array arr[] of size n as input parameters and return the closest number in the array to k. 

// Expected Time Complexity: O(log(n)).
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

public class FindTheClosestNumber {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n;
        n = Integer.parseInt(br.readLine());

        int k;
        k = Integer.parseInt(br.readLine());

        int[] arr = IntArray.input(br, n);

        int res = Solution.findClosest(n, k, arr);

        System.out.println(res);

    }
}

class Solution {
    public static int findClosest(int n, int k, int[] arr) {
        // code here
        int beg = 0, end = n - 1, mid = 0;

        while (beg < end - 1) {
            mid = (beg + end) / 2;
            if (k == arr[mid]) {
                return arr[mid];
            } else if (k < arr[mid]) {
                end = mid;
            } else {
                beg = mid;
            }
        }

        return (k - arr[beg]) < (arr[end] - k) ? arr[beg] : arr[end];
    }
}