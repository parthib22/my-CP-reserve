# GFG POTD 25.08.23

# Given a string S, check if it is palindrome or not.

# Example 1:

# Input: S = "abba"
# Output: 1
# Explanation: S is a palindrome

# Example 2:

# Input: S = "abc"
# Output: 0
# Explanation: S is not a palindrome

# Your Task:
# You don't need to read input or print anything. Complete the function isPalindrome()which accepts string S and returns an integer value 1 or 0.

# Expected Time Complexity: O(Length of S)
# Expected Auxiliary Space: O(1)


class Solution:
    def isPalindrome(self, S):
        i = 0
        for st in S:
            i = i - 1
            if st != S[i]:
                return 0
        return 1


if __name__ == "__main__":
    S = input()
    ob = Solution()
    answer = ob.isPalindrome(S)
    print(answer)
