# https://www.geeksforgeeks.org/problems/count-numbers-containing-43022/1

# Count numbers containing 4

# You are given a number n, Return the count of total numbers from 1 to n containing 4 as a digit.

# Examples:

# Input: n = 9
# Output: 1
# Explanation: 4 is the only number between 1 to 9 which contains 4 as a digit.
# Input: n = 44
# Output: 9
# Explanation: 4, 14, 24, 34, 40, 41, 42, 43 & 44, there are total 9 numbers containing 4 as a digit.
# Expected Time Complexity: O(nlogn)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= n <= 10^5


class Solution:
    def countNumberswith4(self, n: int) -> int:
        # code here
        res = 0
        for i in range(1, n + 1):
            if "4" in str(i):
                res += 1
        return res


if __name__ == "__main__":

    n = int(input())

    obj = Solution()
    res = obj.countNumberswith4(n)

    print(res)
