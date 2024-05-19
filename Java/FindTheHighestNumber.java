// https://www.geeksforgeeks.org/problems/find-the-highest-number2259/1

// POTD 18.05.24

// Find the Highest number

// Given an integer array a[] of size n, find the highest element of the array. The array will either be strictly increasing or strictly increasing and then strictly decreasing.

// Note: a[i] != a[i+1] 

// Example 1:
// Input:
// 11
// 1 2 3 4 5 6 5 4 3 2 1
// Output: 
// 6
// Explanation: 
// Highest element of array a[] is 6.

// Example 2:
// Input:
// 5
// 1 2 3 4 5
// Output:
// 5
// Explanation: 
// Highest element of array a[] is 5.
// Your Task:
// You don't need to read or print anything. Your task is to complete the function findPeakElement() which takes the array a[] as the input parameter and returns the highest element of the array.

// Expected Time Complexity: O(log(n))
// Expected Space Complexity: O(1)

import java.io.*;
import java.util.*;

public class FindTheHighestNumber {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();
        int n = Integer.parseInt(s);
        String S = br.readLine();
        String[] s1 = S.split(" ");
        List<Integer> a = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            a.add(Integer.parseInt(s1[i]));
        }
        Solution ob = new Solution();
        int ans = ob.findPeakElement(a);
        System.out.println(ans);
    }
}

class Solution {
    public int findPeakElement(List<Integer> a) {
        // Code here
        int beg = 0, end = a.size() - 1, mid;

        while (beg < end) {
            mid = (beg + end) / 2;
            if (a.get(mid) < a.get(mid + 1)) {
                beg = mid + 1;
            } else {
                end = mid;
            }
        }
        return a.get(beg);
    }
}