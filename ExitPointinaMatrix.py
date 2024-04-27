# https://www.geeksforgeeks.org/problems/exit-point-in-a-matrix0905/1

# POTD 26.04.2024

# Exit Point in a Matrix

# Given a matrix of size n x m with 0’s and 1’s, you enter the matrix at cell (0,0) in left to right direction. Whenever you encounter a 0 you retain it in the same direction, else if you encounter a 1 you have to change the direction to the right of the current direction and change that 1 value to 0, you have to find out from which index you will leave the matrix at the end.

# Example 1:
# Input:
# n = 3, m = 3
# matrix = {{0, 1, 0},
#           {0, 1, 1},
#           {0, 0, 0}}
# Output:
# {1, 0}
# Explanation:
# Enter the matrix at (0, 0)
# -> then move towards (0, 1) ->  1 is encountered
# -> turn right towards (1, 1)  -> again 1 is encountered
# -> turn right again towards (1, 0)
# -> now, the boundary of matrix will be crossed ->hence, exit point reached at 1, 0..

# Example 2:
# Input:
# n = 1, m = 2
# matrix = {{0, 0}}
# Output:
# {0, 1}
# Explanation:
# Enter the matrix at cell (0, 0).
# Since the cell contains a 0, we continue moving in the same direction.
# We reach cell (0, 1), which also contains a 0. So, we continue moving in the same direction, we exit the matrix from cell (0, 1).
# Your Task:
# You don't need to read or print anything. Your task is to complete the function FindExitPoint() which takes the matrix as an input parameter and returns a list containing the exit point.

# Expected Time Complexity: O(n * m) where n = number of rows and m = number of columns.
# Expected Space Complexity: O(1)


class Solution:
    def FindExitPoint(self, n, m, matrix):
        # Code here

        pointer = [0, 0]
        direction = 1

        i, j = 0, 0
        while i not in [-1, n] and j not in [-1, m]:

            if matrix[i][j] == 1:
                direction += 1
                matrix[i][j] = 0

            if direction > 4:
                direction = 1

            if direction == 1:
                j += 1

            elif direction == 2:
                i += 1

            elif direction == 3:
                j -= 1

            elif direction == 4:
                i -= 1

            pointer = [i, j]

            if pointer[0] == -1:
                pointer[0] = 0

            if pointer[0] == n:
                pointer[0] = n - 1

            if pointer[1] == -1:
                pointer[1] = 0

            if pointer[1] == m:
                pointer[1] = m - 1

            return pointer


if __name__ == "__main__":
    n, m = input().split()
    n = int(n)
    m = int(m)
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    ob = Solution()
    ans = ob.FindExitPoint(n, m, matrix)
    for _ in ans:
        print(_, end=" ")
    print()
