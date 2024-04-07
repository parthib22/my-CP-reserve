# https://www.geeksforgeeks.org/problems/insert-an-element-at-the-bottom-of-a-stack/1

# POTD 24.03.2024

# Insert an element at the bottom of a stack

# You are given a stack st of n integers and an element x. You have to insert x at the bottom of the given stack.

# Note: Everywhere in this problem, the bottommost element of the stack is shown first while priniting the stack.

# Example 1:
# Input:
# n = 5
# x = 2
# st = {4,3,2,1,8}
# Output:
# {2,4,3,2,1,8}
# Explanation:
# After insertion of 2, the final stack will be {2,4,3,2,1,8}.

# Example 2:
# Input:
# n = 3
# x = 4
# st = {5,3,1}
# Output:
# {4,5,3,1}
# Explanation:
# After insertion of 4, the final stack will be {4,5,3,1}.
# Your Task:

# You don't need to read input or print anything. Your task is to complete the function insertAtBottom() which takes a stack st and an integer x as inputs and returns the modified stack after insertion.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)


class Solution:
    def insertAtBottom(self, st, x):
        # code here
        return [x] + st
        # st.insert(0, x)
        # return st


if __name__ == "__main__":
    n, x = map(int, input().split())
    stack = list(map(int, input().split()))
    obj = Solution()
    ans = obj.insertAtBottom(stack, x)
    for e in ans:
        print(e, end=" ")
    print()
