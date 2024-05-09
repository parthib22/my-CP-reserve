# https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1

# POTD 08.05.2024

# Root to Leaf Paths

# Given a Binary Tree of nodes, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

# Example 1:
# Input:
#        1
#     /     \
#    2       3
# Output:
# 1 2
# 1 3
# Explanation:
# All possible paths:
# 1->2
# 1->3

# Example 2:
# Input:
#          10
#        /    \
#       20    30
#      /  \
#     40   60
# Output:
# 10 20 40
# 10 20 60
# 10 30
# Your Task:
# Your task is to complete the function Paths() which takes the root node as an argument and returns all the possible paths. (All the paths are printed in new lines by the driver's code.)

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(height of the tree)

from typing import Optional
from collections import deque

from typing import List


class Solution:
    def Paths(self, root: Optional["Node"]) -> List[List[int]]:
        # code here
        ans = []

        def rec(node, path):
            if not node:
                return
            if not node.left and not node.right:
                ans.append(path + [node.data])
                return
            if node.left:
                rec(node.left, path + [node.data])
            if node.right:
                rec(node.right, path + [node.data])

        rec(root, [])
        return ans


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


def inputTree():
    treeString = input().strip()
    root = buildTree(treeString)
    return root


def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":

    root = inputTree()

    obj = Solution()
    res = obj.Paths(root)

    IntMatrix().Print(res)
