# https://www.geeksforgeeks.org/problems/generalised-fibonacci-numbers1820/1

# POTD 12.03.2024

# Generalised Fibonacci numbers

# Consider the generalized Fibonacci number g, which is dependent on a, b and c as follows :-
# g(1) = 1, g(2) = 1. For any other number n, g(n) = a*g(n-1) + b*g(n-2) + c.

# For a given value of m, determine g(n)%m.

# Example 1:

# Input:
# a = 3
# b = 3
# c = 3
# n = 3
# m = 5
# Output:
# 4
# Explanation:
# g(1) = 1 and g(2) = 1
# g(3) = 3*g(2) + 3*g(1) + 3 = 3*1 + 3*1 + 3 = 9
# We need to return answer modulo 5, so 9%5 = 4, is the answer.
# Example 2:

# Input:
# a = 2
# b = 2
# c = 2
# n = 4
# m = 100
# Output:
# 16
# Explanation:
# g(1) = 1 and g(2) = 1
# g(3) = 2*g(2) + 2*g(1) + 2 = 2*1 + 2*1 + 2 = 6
# g(4) = 2*g(3) + 2*g(2) + 2  = 2*6 + 2*1 + 2 = 16
# We need to return answer modulo 100, so 16%100 = 16, is the answer.
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function genFibNum() which takes 5 Integers a, b, c, n, and m as input and returns g(n)%m.

# Expected Time Complexity: O( log(n) ).
# Expected Auxiliary Space: O(1).


class Solution:
    # def genFibNum(self, a, b, c, n, m):
    #     # code here
    #     if [a, b, c, n, m].count(a) == 5:
    #         return 0
    #     def g(n: int) -> int:
    #         if n == 1 or n == 2:
    #             return 1
    #         else:
    #             return a * g(n - 1) + b * g(n - 2)
    #     return (g(n) + c) % m

    def multiply(self, A, B, m):
        size = len(A)
        result = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    result[i][j] += A[i][k] * B[k][j]
                    result[i][j] %= m
        return result

    def genFibNum(self, a, b, c, n, m):
        if n <= 2:
            return 1 % m
        mat = [[a, b, 1], [1, 0, 0], [0, 0, 1]]
        res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        n -= 2
        while n > 0:
            if n & 1:
                res = self.multiply(res, mat, m)
            mat = self.multiply(mat, mat, m)
            n >>= 1
        return (res[0][0] + res[0][1] + c * res[0][2]) % m


if __name__ == "__main__":
    a, b, c, n, m = map(int, input().split())
    print(Solution().genFibNum(a, b, c, n, m))
