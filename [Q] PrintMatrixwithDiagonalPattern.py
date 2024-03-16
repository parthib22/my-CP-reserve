# https://www.geeksforgeeks.org/problems/print-matrix-in-diagonal-pattern/1

# POTD 13.03.2024

# Print matrix in diagonal pattern

# Given a square matrix mat[][] of n*n size, the task is to determine the diagonal pattern which is a linear arrangement of the elements of the matrix as depicted in the following example:

# https://contribute.geeksforgeeks.org/wp-content/uploads/matrix-6.png

# Example 1:

# Input:
# n = 3
# mat[][] = {{1, 2, 3},
#            {4, 5, 6},
#            {7, 8, 9}}
# Output: {1, 2, 4, 7, 5, 3, 6, 8, 9}
# Explaination:
# Starting from (0, 0): 1,
# Move to the right to (0, 1): 2,
# Move diagonally down to (1, 0): 4,
# Move diagonally down to (2, 0): 7,
# Move diagonally up to (1, 1): 5,
# Move diagonally up to (0, 2): 3,
# Move to the right to (1, 2): 6,
# Move diagonally up to (2, 1): 8,
# Move diagonally up to (2, 2): 9
# There for the output is {1, 2, 4, 7, 5, 3, 6, 8, 9}.

# Example 2:

# Input:
# n = 2
# mat[][] = {{1, 2},
#            {3, 4}}
# Output: {1, 2, 3, 4}
# Explaination:
# Starting from (0, 0): 1,
# Move to the right to (0, 1): 2,
# Move diagonally down to (1, 0): 3,
# Move to the right to (1, 1): 4
# There for the output is {1, 2, 3, 4}.
# Your Task:
# You only need to implement the given function matrixDiagonally() which takes a matrix mat[][] of size n*n as an input and returns a list of integers containing the matrix diagonally. Do not read input, instead use the arguments given in the function.

# Expected Time Complexity: O(n*n).
# Expected Auxiliary Space: O(1).


class Solution:
    def matrixDiagonally(self, mat):
        # code here
        self.n = len(mat)
        self.pattern = []

        # Flag to indicate upward or downward traversal
        upward = False

        for i in range(self.n):
            if upward:
                # Traverse upwards
                row, col = 0, i
                while col >= 0:
                    self.pattern.append(mat[row][col])
                    row += 1
                    col -= 1
                upward = False
            else:
                # Traverse downwards
                row, col = i, 0
                while row >= 0:
                    self.pattern.append(mat[row][col])
                    row -= 1
                    col += 1
                upward = True

        for i in range(1, self.n):
            if upward:
                # Traverse upwards
                row, col = i, self.n - 1
                while row < self.n:
                    self.pattern.append(mat[row][col])
                    row += 1
                    col -= 1
                upward = False
            else:
                # Traverse downwards
                row, col = self.n - 1, i
                while col < self.n:
                    self.pattern.append(mat[row][col])
                    row -= 1
                    col += 1
                upward = True

        return self.pattern


if __name__ == "__main__":
    n = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    matrix = [[0 for i in range(n[0])] for j in range(n[0])]
    k = 0
    for i in range(n[0]):
        for j in range(n[0]):
            matrix[i][j] = arr[k]
            k += 1
    a = Solution().matrixDiagonally(matrix)
    for x in a:
        print(x, end=" ")
    print("")
