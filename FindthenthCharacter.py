# GFG POTD 08.03.2024
# https://www.geeksforgeeks.org/problems/find-the-n-th-character5925/1

# Find the N-th character

# Given a binary string s. Perform r iterations on string s, where in each iteration 0 becomes 01 and 1 becomes 10. Find the nth character (considering 0 based indexing) of the string after performing these r iterations (see examples for better understanding).

# Example 1:
# Input:
# s = "1100"
# r = 2
# n = 3
# Output:
# 1
# Explanation:
# After 1st iteration s becomes "10100101".
# After 2nd iteration s becomes "1001100101100110".
# Now, we can clearly see that the character at 3rd index is 1, and so the output.

# Example 2:
# Input:
# s = "1010"
# r = 1
# n = 2
# Output:
# 0
# Explanation :
# After 1st iteration s becomes "10011001".
# Now, we can clearly see that the character at 2nd index is 0, and so the output.
# Your task:
# You don't need to read input or print anything. Your task is to complete the function nthCharacter() which takes the string s and integers r and n as input parameters and returns the n-th character of the string after performing r operations on s.

# Expected Time Complexity: O(r*|s|)
# Expected Auxilary Space: O(|s|)


class Solution:
    def nthCharacter(self, s, r, n):
        s2 = ""
        while r > 0:
            for i in range(n + 1):
                if s[i] == "1":
                    s2 += "10"
                elif s[i] == "0":
                    s2 += "01"
            s = s2
            s2 = ""
            r -= 1
        return s[n]


if __name__ == "__main__":
    snr = input().split()
    S, R, N = snr[0], int(snr[1]), int(snr[2])
    ob = Solution()
    print(ob.nthCharacter(S, R, N))
