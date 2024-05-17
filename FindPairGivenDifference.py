# https://www.geeksforgeeks.org/problems/find-pair-given-difference1559/1

# POTD 17.05.24

# Find Pair Given Difference

# Given an array arr[] of size n and an integer x, return 1 if there exists a pair of elements in the array whose absolute difference is x, otherwise, return -1.

# Example 1:

# Input:
# n = 6
# x = 78
# arr[] = {5, 20, 3, 2, 5, 80}
# Output:
# 1
# Explanation:
# Pair (2, 80) have absolute difference of 78.
# Example 2:

# Input:
# n = 5
# x = 45
# arr[] = {90, 70, 20, 80, 50}
# Output:
# -1
# Explanation:
# There is no pair with absolute difference of 45.
# Your Task:
# You need not take input or print anything. Your task is to complete the function findPair() which takes integers n, x, and an array arr[] as input parameters and returns 1 if the required pair exists, return -1 otherwise.

# Expected Time Complexity: O(n* Log(n)).
# Expected Auxiliary Space: O(1).

from typing import List


class Solution:

    def findPair(self, n: int, x: int, arr: List[int]) -> int:

        # code here

        s = set(arr)

        if x == 0 and len(arr) == len(s):
            return -1

        for i in range(n):
            if (arr[i] + x) in s or (arr[i] - x) in s:
                return 1

        return -1


class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":

    n = int(input())

    x = int(input())

    arr = IntArray().Input(n)

    obj = Solution()
    res = obj.findPair(n, x, arr)

    print(res)
