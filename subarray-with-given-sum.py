# GFG POTD 19.08.23

# Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

# In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

# Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

# Your Task:
# You don't need to read input or print anything. The task is to complete the function subarraySum() which takes arr, N, and S as input parameters and returns an ArrayList containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S. The two indexes in the array should be according to 1-based indexing. If no such subarray is found, return an array consisting of only one element that is -1.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements from 2nd position to 4th position is 12.

import math


class Solution:
    def subArraySum(self, arr, n, s):
        b = 0
        e = 0
        k = 0
        if s == 0:
            return [-1]
        while e < n:
            k = k + arr[e]
            while k > s and b <= e:
                k = k - arr[b]
                b = b + 1
            if k == s:
                return [b + 1, e + 1]
            e = e + 1
        return [-1]

        # f=0
        # k=0
        # for i in range(n-1):
        #     k=0
        #     for j in range(i,n):
        #         k= k+arr[j]
        #         if k == s:
        #             f=1
        #             return [i+1,j+1]
        #         if k>s:
        #             break
        #     if i == 0 and k<s:
        #         return [-1]
        # return [-1]


def main():
    T = int(input())
    while T > 0:
        NS = input().strip().split()
        N = int(NS[0])
        S = int(NS[1])

        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.subArraySum(A, N, S)

        for i in ans:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
