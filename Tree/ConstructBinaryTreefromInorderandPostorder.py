# https://www.geeksforgeeks.org/problems/tree-from-postorder-and-inorder/1

# POTD 04.05.2024

# Construct Binary Tree from Inorder and Postorder

# Given inorder and postorder traversals of a binary tree(having n nodes) in the arrays in[] and post[] respectively. The task is to construct a binary tree from these traversals.

# Driver code will print the preorder traversal of the constructed tree.

# Example 1:
# Input:
# n = 8
# in[] = {4, 8, 2, 5, 1, 6, 3, 7}
# post[] = {8, 4, 5, 2, 6, 7, 3, 1}
# Output:
# 1 2 4 8 5 3 6 7
# Explanation:
# For the given postorder and inorder traversal of tree the  resultant binary tree will be
#           1
#        /      \
#      2        3
#    /  \      /  \
#   4   5    6   7
#    \
#     8

# Example 2:
# Input:
# n = 5
# in[] = {9, 5, 2, 3, 4}
# post[] = {5, 9, 3, 4, 2}
# Output:
# 2 9 5 4 3
# Explanation:
# The  resultant binary tree will be
#            2
#         /     \
#        9      4
#         \     /
#          5   3
# Your Task:
# You do not need to read input or print anything. Complete the function buildTree() which takes the inorder, postorder traversals and the number of nodes in the tree as input parameters and returns the root node of the newly constructed Binary Tree.

# Expected Time Complexity: O(n2)
# Expected Auxiliary Space: O(n)


class Solution:
    def buildTree(self, In, post, n):
        if not In or not post:
            return None
        idx = In.index(post[-1])
        root = Node(post[-1])
        root.left = self.buildTree(In[:idx], post[:idx], n)
        root.right = self.buildTree(In[idx + 1 :], post[idx:-1], n)
        return root


import atexit
import io
import sys
from collections import defaultdict

# Contributed by : PranchalK


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Helper function that allocates
# a new node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# This funtcion is here just to test
def preOrder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preOrder(node.left)
    preOrder(node.right)


if __name__ == "__main__":
    n = int(input())  # number of nodes in tree
    in_order = list(map(int, input().strip().split()))  # parent child info in list
    post_order = list(map(int, input().strip().split()))  # parent child info in list
    ob = Solution()
    preOrder(ob.buildTree(in_order, post_order, n))
