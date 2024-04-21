# https://www.geeksforgeeks.org/problems/three-way-partitioning/1

# POTD 21.04.2024

# Three way partitioning

# Given an array of size n and a range [a, b]. The task is to partition the array around the range such that the array is divided into three parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order. You are required to return the modified array.

# Note: The generated output is 1 if you modify the given array successfully.

# Geeky Challenge: Solve this problem in O(n) time complexity.

# Example 1:
# Input:
# n = 5
# array[] = {1, 2, 3, 3, 4}
# [a, b] = [1, 2]
# Output:
# 1
# Explanation:
# One possible arrangement is: {1, 2, 3, 3, 4}. If you return a valid arrangement, output will be 1.

# Example 2:
# Input:
# n = 6
# array[] = {1, 4, 3, 6, 2, 1}
# [a, b] = [1, 3]
# Output:
# 1
# Explanation:
# One possible arrangement is: {1, 3, 2, 1, 4, 6}. If you return a valid arrangement, output will be 1.
# Your Task:
# You don't need to read input or print anything. The task is to complete the function threeWayPartition() which takes the array array, a, and b as input parameters and modifies the array in place according to the given conditions.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= n <= 10^6
# 1 <= array[i], a, b <= 10^9


class Solution:
    # Function to partition the array around the range such
    # that array is divided into three parts.
    def threeWayPartition(self, array, a, b):
        # code here
        index = 0

        def inRange(x, y):
            nonlocal index
            for i in range(len(array)):
                if array[i] in range(x, y):
                    array[i], array[index] = array[index], array[i]
                    index += 1
            return

        inRange(1, a)  # less than a
        inRange(a, b + 1)  # between a and b
        inRange(b + 1, 10**9 + 1)  # greater than b

        # python one line solution
        # return array.sort()


from collections import Counter

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().strip().split()))
    original = Counter(array)
    a, b = list(map(int, input().strip().split()))
    ob = Solution()
    ob.threeWayPartition(array, a, b)

    k1 = k2 = k3 = 0
    for e in array:
        if e > a:
            k3 += 1
        elif e <= a and e >= b:
            k2 += 1
        elif e < a:
            k1 += 1

    m1 = m2 = m3 = 0
    for e in range(k1):
        if array[e] < a:
            m1 += 1
    for e in range(k1, k1 + k2):
        if array[e] <= a and array[e] >= b:
            m2 += 1
    for e in range(k1 + k2, k1 + k2 + k3):
        if array[e] >= a:
            m3 += 1

    flag = False
    if k1 == m1 and k2 == m2 and k3 == m3:
        flag = True
    for e in range(len(array)):
        original[array[e]] -= 1
    for e in range(len(array)):
        if original[array[e]] != 0:
            flag = False
    if flag:
        print(1)
    else:
        print(0)
