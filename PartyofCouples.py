# https://www.geeksforgeeks.org/problems/alone-in-couple5507/1

# POTD 10.04.2024

# Party of Couples

# You are given an integer array arr[] of size n, representing n number of people in a party, each person is denoted by an integer. Couples are represented by the same number ie: two people have the same integer value, it means they are a couple. Find out the only single person in the party of couples.

# NOTE: It is guarantee that there exist only one single person in the party.

# Example 1:
# Input:
# n = 5
# arr = {1, 2, 3, 2, 1}
# Output:
# 3
# Explaination: Only the number 3 is single.

# Example 2:
# Input:
# n = 11
# arr = {1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6}
# Output:
# 4
# Explaination: 4 is the only single.
# Your Task:
# You do not need to read input or print anything. Your task is to complete the function findSingle() which takes the size of the array n and the array arr[] as input parameters and returns the only single person.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# from functools import reduce


class Solution:
    def findSingle(self, n, arr):
        # code here
        hashmap = {}
        for a in arr:
            if a not in hashmap:
                hashmap[a] = 0
            hashmap[a] += 1
        for key, value in hashmap.items():
            if value % 2 > 0:
                return key

    # def findSingle(self, n, arr):
    #     single_person = 0
    #     for num in arr:
    #         single_person ^= num
    #     return single_person

    # def findSingle(self, n, arr):
    #     return reduce(lambda x, y: x ^ y, arr, 0)


if __name__ == "__main__":
    N = int(input())
    arr = input().split()
    for itr in range(N):
        arr[itr] = int(arr[itr])

    ob = Solution()
    print(ob.findSingle(N, arr))
