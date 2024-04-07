// https://www.geeksforgeeks.org/problems/additive-sequence/1

// Additive sequence

// Given a string n, your task is to find whether it contains an additive sequence or not. A string n contains an additive sequence if its digits can make a sequence of numbers in which every number is addition of previous two numbers (within the range of signed integers). You are required to complete the function which returns true if the string is a valid sequence else returns false. For better understanding check the examples.

// Note: A valid string should contain at least three digit to make one additive sequence. 

// Example 1:
// Input:  
// n = "1235813"
// Output: 
// 1
// Explanation: 
// The given string can be splited into a series of numbers  
// where each number is the sum of the previous two numbers: 
// 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8, and 5 + 8 = 13. Hence, the output would be 1 (true).

// Example 2:
// Input:  
// n = "11235815"
// Output: 
// 0
// Explanation: 
// We can start with the first two digits: "11".
// First number: 1, Second number: 1, Sum: 1 + 1 = 2
// Now, we have "2" as the next number.
// First number: 1, Second number: 2, Sum: 1 + 2 = 3
// Now, we have "3" as the next number.
// First number: 2, Second number: 3, Sum: 2 + 3 = 5
// Now, we have "5" as the next number.
// First number: 3, Second number: 5, Sum: 3 + 5 = 8
// Now, we have "8" as the next number.
// First number: 5, Second number: 8, Sum: 5 + 8 = 13
// At this point, there is no "13" present in the remaining digits "815". Hence, the output would be 0 (or false).
// User Task: 
// Your task is to complete the function isAdditiveSequence() which takes a single string as input n and returns a boolean value indicating whether the given string contains an additive sequence or not. You need not take any input or print anything.

// Expected Time Complexity: O(n3).
// Expected Auxiliary Space: O(n).

import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            String s = sc.next();
            Solution ss = new Solution();
            boolean result = ss.isAdditiveSequence(s);
            System.out.println((result == true ? 1 : 0));
        }
        sc.close();
    }
}

class Solution {
    public boolean isAdditiveSequence(String n) {
        // code here
        int num1 = 0;
        int size = n.length();
        for (int i = 0; i < (size / 2); i++) {
            num1 = num1 * 10 + (n.charAt(i) - '0');
            int num2 = 0;
            for (int j = i + 1; j < size - 1; j++) {
                num2 = num2 * 10 + (n.charAt(j) - '0');
                int first = num1, second = num2, num3 = 0;
                int k = j + 1;
                while (k < size) {
                    num3 = num3 * 10 + (n.charAt(k) - '0');
                    if (num3 == first + second) {
                        first = second;
                        second = num3;
                        num3 = 0;
                    }
                    k++;
                }
                if (k == size && num3 == 0) {
                    return true;
                }
            }
        }
        return false;
    }
}