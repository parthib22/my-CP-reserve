# GFG POTD 17.08.23
# https://practice.geeksforgeeks.org/problems/next-smallest-palindrome4740/1

# Given a number, in the form of an array Num[] of size N containing digits from 1 to 9(inclusive). The task is to find the next smallest palindrome strictly larger than the given number.

# Your Task:
# Complete the function generateNextPalindrome() which takes an array num, and a single integer n, as input parameters and returns an array of integers denoting the answer. You don't to print answer or take inputs.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Example 1:

# Input:
# N = 11
# Num[] = {9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2}
# Output: 9 4 1 8 8 0 8 8 1 4 9
# Explanation: Next smallest palindrome is
# 9 4 1 8 8 0 8 8 1 4 9

# Example 2:

# Input:
# N = 5
# Num[] = {2, 3, 5, 4, 5}
# Output: 2 3 6 3 2
# Explanation: Next smallest palindrome is
# 2 3 6 3 2


class Solution:
    def generateNextPalindrome(self, num, n):
        # code here
        m = n // 2
        p = m
        L = []
        L = num[:m]
        if n == 1:
            return L
        if n % 2 == 0:
            if num[m - 1] < num[m]:
                L[-1] = L[-1] + 1
        else:
            L.append(num[m])
            if num[m - 1] <= num[m + 1]:
                L[-1] = L[-1] + 1
            while L[p] > 9:
                L[p], L[p - 1], p = 0, L[p - 1] + 1, p - 1
        for i in range(m - 1, -1, -1):
            L.append(L[i])
        return L

        # m = n // 2
        # k = m
        # L = []
        # for i in range(m):
        #     L.append(num[i])
        # if n % 2 != 0:
        #     if num[m - 1] < num[m + 1]:
        #         if num[m] < 9:
        #             L.append(num[m] + 1)
        #         else:
        #             L.append(num[m])
        #             while L[k] == 9 and k >= 0:
        #                 L[k] = 0
        #                 k = k - 1
        #                 L[k] = L[k] + 1
        #     else:
        #         L.append(num[m])
        # else:
        #     # use slicing tomorrow
        #     if num[m] < num[m + 1]:
        #         if num[m] < 9:
        #             L[m] = L[m] + 1
        #         else:
        #             while L[k] == 9 and k >= 0:
        #                 L[k] = 0
        #                 k = k - 1
        #                 L[k] = L[k] + 1
        # for i in range(m - 1, -1, -1):
        #     L.append(L[i])
        # return L


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        num = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.generateNextPalindrome(num, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc - 1
