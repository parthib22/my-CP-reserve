# https://www.geeksforgeeks.org/problems/compare-two-fractions4438/1

# Compare two fractions

# You are given a string str containing two fractions a/b and c/d, compare them and return the greater. If they are equal, then return "equal".

# Note: The string str contains "a/b, c/d"(fractions are separated by comma(,) & space( )).

# Examples

# Input: str = "5/6, 11/45"
# Output: 5/6
# Explanation: 5/6=0.8333 and 11/45=0.2444, So 5/6 is greater fraction.
# Input: str = "8/1, 8/1"
# Output: equal
# Explanation: We can see that both the fractions are same, so we'll return a string "equal".
# Input: str = "10/17, 9/10"
# Output: 9/10
# Explanation: 10/17 = 0.588 & 9/10 = 0.9, so the greater fraction is "9/10".
# Expected Time Complexity: O(len|str|)
# Expected Auxiliary Space: O(1)

# Constraints:
# 0<=a,c<=10^3
# 1<=b,d<=10^3


class Solution:
    def compareFrac(self, str):
        # code here
        # a, b, c, d = map(int, str.replace(',', ' ').split())
        # if a*d > b*c:
        #     return f"{a}/{b}"
        # elif a*d < b*c:
        #     return f"{c}/{d}"
        # return "equal"

        fra1, fra2 = str.split(", ")

        tmp = fra1.split("/")
        num1 = int(tmp[0]) / int(tmp[1])

        tmp = fra2.split("/")
        num2 = int(tmp[0]) / int(tmp[1])

        if num1 == num2:
            return "equal"

        return fra1 if num1 > num2 else fra2


import re

if __name__ == "__main__":
    ob = Solution()
    str = input()
    print(ob.compareFrac(str))
