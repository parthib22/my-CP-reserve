# https://www.geeksforgeeks.org/problems/maximum-sum-of-hour-glass3842/1

# POTD 25.04.2024

# Maximum sum of hour glass

# Given two integers n, m and a 2D matrix mat of dimensions nxm, the task is to find the maximum sum of an hourglass.
# An hourglass is defined as a part of the matrix with the following form:

# Return -1 if any hourglass is not found.

# Example 1:
# Input:
# n = 3, m = 3
# mat = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
# Output:
# 35
# Explanation:
# There is only one hour glass which is
# 1 2 3
#   5
# 7 8 9   and its sum is 35.

# Example 2:
# Input:
# n = 2, m = 3
# mat = [[1, 2, 3],
#        [4, 5, 6]]
# Output:
# -1
# Explanation:
# There are no hour glasses in this matrix.
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function findMaxSum() which takes the two integers n, m, and the 2D matrix mat as input parameters and returns the maximum sum of an hourglass in the matrix. If there are no hourglasses, it returns -1.

# Expected Time Complexity: O(n*m)
# Expected Auxillary Space: O(1)


class Solution:
    def findMaxSum(self, n, m, mat):
        # code here

        if n < 3 or m < 3:
            return -1

        max_sum = float("-inf")

        for i in range(n - 2):
            for j in range(m - 2):

                hourglass_sum = (
                    mat[i][j]
                    + mat[i][j + 1]
                    + mat[i][j + 2]
                    + mat[i + 1][j + 1]
                    + mat[i + 2][j]
                    + mat[i + 2][j + 1]
                    + mat[i + 2][j + 2]
                )

                max_sum = max(max_sum, hourglass_sum)

        if max_sum == float("-inf"):
            return -1
        else:
            return max_sum

        # if n < 3:
        #     return -1

        # row = 0
        # col = 0
        # _max = float('-inf')

        # while True:
        #     sum = 0
        #     if row > n - 3:
        #         break
        #     elif col > m - 3:
        #         col = 0
        #         row += 1
        #     else:
        #         for i in range(row, row+3):
        #             for j in range(col, col+3):
        #                 if not (i == row + 1 and j != col + 1):
        #                     sum += mat[i][j]
        #         _max = max(_max, sum)
        #         col += 1

        # return _max


import math

if __name__ == "__main__":
    N, M = map(int, input().strip().split(" "))
    Mat = []
    for i in range(N):
        B = list(map(int, input().strip().split(" ")))
        Mat.append(B)
    ob = Solution()
    ans = ob.findMaxSum(N, M, Mat)
    print(ans)
