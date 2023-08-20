# GFG POTD 18.08.23

# Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader.

# Your Task:
# You don't need to read input or print anything. The task is to complete the function leader() which takes array A and n as input parameters and returns an array of leaders in order of their appearance.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)

# Input:
# n = 6
# A[] = {16,17,4,3,5,2}
# Output: 17 5 2
# Explanation: The first leader is 17 as it is greater than all the elements to its right. Similarly, the next leader is 5. The right most element is always a leader so it is also included.

import math


class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, A, N):
        L = []
        mx = A[-1]
        for i in range(1, N + 1):
            if mx <= A[-i]:
                mx = A[-i]
                L.append(A[-i])
        L.reverse()
        return L

        # L=[]
        # i=0
        # while i < N-1:
        #     j=i+1
        #     while A[i]>=A[j]:
        #         if j==N-1:
        #             L.append(A[i])
        #             break
        #         j=j+1
        #     i=i+1
        # L.append(A[-1])
        # return L


def main():
    T = int(input())

    while T > 0:
        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(A, N)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
