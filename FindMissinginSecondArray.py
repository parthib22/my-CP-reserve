# https://www.geeksforgeeks.org/problems/in-first-but-second5423/1

# POTD 19.04.2024

# Find missing in second array

# Given two arrays a of size n and b of size m, the task is to find numbers which are present in the first array, but not present in the second array.

# Example 1:
# Input:
# n = 6, m = 5
# a[] = {1, 2, 3, 4, 5, 10}
# b[] = {2, 3, 1, 0, 5}
# Output:
# 4 10
# Explanation:
# 4 and 10 are present in first array, but not in second array.

# Example 2:
# Input:
# n = 5, m = 5
# a[] = {4, 3, 5, 9, 11}
# b[] = {4, 9, 3, 11, 10}
# Output:
# 5
# Explanation:
# Second array does not contain element 5.
# Your Task:
# This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function findMissing() that takes array a, array b, integer n, and integer m as parameters and returns an array that contains the missing elements and the order of the elements should be the same as they are in array a.

# Expected Time Complexity: O(n+m).
# Expected Auxiliary Space: O(m).


class Solution:
    def findMissing(self, a, b, n, m):
        # code here
        b_set = set(b)
        return [_a for _a in a if _a not in b_set]

        d = {}
        for i in range(n):
            d[a[i]] = 0
        for i in range(m):
            if b[i] in d:
                d[b[i]] = 1

        # print(d)

        res = []

        # for _a in a:
        #     if _a not in b:
        #         res.append(_a)

        for key, val in d.items():
            if val == 0:
                res.append(key)

        return res


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(*Solution().findMissing(a, b, n, m))
