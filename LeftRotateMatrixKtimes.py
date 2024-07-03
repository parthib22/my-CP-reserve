# https://www.geeksforgeeks.org/problems/left-rotate-matrix-k-times2351/1

# Left Rotate Matrix K times

# You are given an integer k and matrix mat. Rotate the elements of the given matrix to the left k times and return the resulting matrix.

# Examples:

# Input: k=1, mat=[[1,2,3],[4,5,6],[7,8,9]]
# Output:
# 2 3 1
# 5 6 4
# 8 9 7
# Explanation: Rotate the matrix by one
# 1 2 3       2 3 1
# 4 5 6  =>  5 6 4
# 7 8 9       8 9 7
# Input: k=2, mat=[[1,2,3],[4,5,6],[7,8,9]]
# Output:
# 3 1 2
# 6 4 5
# 9 7 8
# Explanation: After rotating the matrix looks like
# 1 2 3       2 3 1       3 1 2
# 4 5 6  =>  5 6 4  =>   6 4 5
# 7 8 9       8 9 7       9 7 8
# Expected Time Complexity: O(n*m)
# Expected Auxillary Space: O(n*m)

# Constraints:
# 1<= mat.size, mat[0].size, mat[i][j] <=1000
# 1<=k<=10000


class Solution:
    def rotateMatrix(self, k, mat):

        k = k % len(mat[0])

        for i in range(len(mat)):
            mat[i] = mat[i][k:] + mat[i][:k]

        return mat


import math

if __name__ == "__main__":
    n, m, k = map(int, input().strip().split(" "))
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().strip().split(" "))))
    ob = Solution()
    ans = ob.rotateMatrix(k, mat)
    for i in range(n):
        for j in range(m):
            print(ans[i][j], end=" ")
        print()
