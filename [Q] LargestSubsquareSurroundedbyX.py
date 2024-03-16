# https://www.geeksforgeeks.org/problems/largest-subsquare-surrounded-by-x0558/1

# POTD 14.03.2024

# Largest subsquare surrounded by X

# Given a square matrix a of size n x n, where each cell can be either 'X' or 'O', you need to find the size of the largest square subgrid that is completely surrounded by 'X'. More formally you need to find the largest square within the grid where all its border cells are 'X'.

# Example 1:
# Input:
# n = 2
# a = [[X,X],
#      [X,X]]
# Output:
# 2
# Explanation:
# The largest square submatrix
# surrounded by X is the whole
# input matrix.

# Example 2:
# Input:
# n = 4
# a = [[X,X,X,O],
#      [X,O,X,X],
#      [X,X,X,O],
#      [X,O,X,X]]
# Output:
# 3
# Explanation:
# Here,the input represents following
# matrix of size 4 x 4
# X X X O
# X O X X
# X X X O
# X O X X
# The square submatrix starting at
# (0,0) and ending at (2,2) is the
# largest submatrix surrounded by X.
# Therefore, size of that matrix would be 3.
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function largestSubsquare() which takes the integer n and the matrix a as input parameters and returns the size of the largest subsquare surrounded by 'X'.

# Expected Time Complexity: O(n2)
# Expected Auxillary Space: O(n2)


class Solution:
    def largestSubsquare(self, n, a):
        # Initialize matrices for top and left counts
        top = [[0 for _ in range(n)] for _ in range(n)]
        left = [[0 for _ in range(n)] for _ in range(n)]

        # Compute top metric
        for i in range(n):
            for j in range(n):
                if a[i][j] == "X":
                    top[i][j] = 1 if i == 0 else top[i - 1][j] + 1

        # Compute left metric
        for i in range(n):
            for j in range(n):
                if a[i][j] == "X":
                    left[i][j] = 1 if j == 0 else left[i][j - 1] + 1

        # Finding the largest subsquare
        maxSubSq = 0
        for i in range(n):
            for j in range(n):
                if top[i][j] == 0 or left[i][j] == 0:
                    continue

                currentValue = min(top[i][j], left[i][j])

                while currentValue > 0:
                    top1 = i - currentValue + 1
                    left1 = j - currentValue + 1

                    if left[top1][j] >= currentValue and top[i][left1] >= currentValue:
                        maxSubSq = max(maxSubSq, currentValue)
                        break

                    currentValue -= 1

        return maxSubSq


import math

if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        s = list(map(str, input().strip().split()))
        a.append(s)
    ob = Solution()
    print(ob.largestSubsquare(n, a))
