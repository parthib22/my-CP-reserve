# GFG POTD 10.03.2024
# https://www.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1

# Remove all duplicates from a given string

# Given a string str which may contains lowercase and uppercase chracters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.

# Example 1:
# Input:
# str = "geEksforGEeks"
# Output:
# "geEksforG"
# Explanation:
# After removing duplicate characters such as E, e, k, s, we have string as "geEksforG".

# Example 2:
# Input:
# str = "HaPpyNewYear"
# Output:
# "HaPpyNewYr"
# Explanation:
# After removing duplicate characters such as e, a, we have string as "HaPpyNewYr".
# Your Task:
# Complete the function removeDuplicates() which takes a string str, as input parameters and returns a string denoting the answer. You don't have to print answer or take inputs.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)


class Solution:
    def removeDuplicates(self, str: str) -> str:
        s = ""
        for i in range(len(str)):
            if str[i] not in s:
                s = s + str[i]
        return s


if __name__ == "__main__":
    str = input().strip()
    ob = Solution()
    ans = ob.removeDuplicates(str)
    print(ans)
