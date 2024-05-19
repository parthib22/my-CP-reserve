# https://www.geeksforgeeks.org/problems/find-the-highest-number2259/1

# POTD 18.05.24

# Find the Highest number

# Given an integer array a[] of size n, find the highest element of the array. The array will either be strictly increasing or strictly increasing and then strictly decreasing.

# Note: a[i] != a[i+1]

# Example 1:
# Input:
# 11
# 1 2 3 4 5 6 5 4 3 2 1
# Output:
# 6
# Explanation:
# Highest element of array a[] is 6.

# Example 2:
# Input:
# 5
# 1 2 3 4 5
# Output:
# 5
# Explanation:
# Highest element of array a[] is 5.
# Your Task:
# You don't need to read or print anything. Your task is to complete the function findPeakElement() which takes the array a[] as the input parameter and returns the highest element of the array.

# Expected Time Complexity: O(log(n))
# Expected Space Complexity: O(1)

from typing import List


class Solution:
    def findPeakElement(self, a):
        # Code here

        # return max(set(a))

        beg = 0
        end = len(a) - 1

        while beg < end:
            mid = (beg + end) // 2
            if a[mid] < a[mid + 1]:
                beg = mid + 1
            else:
                end = mid

            return a[beg]
