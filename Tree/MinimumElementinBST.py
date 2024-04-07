# https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1

# Minimum element in BST

# Given the root of a Binary Search Tree. The task is to find the minimum valued element in this given BST.

# Example 1:
# Input:
#            5
#          /    \
#         4      6
#        /        \
#       3          7
#      /
#     1
# Output: 1

# Example 2:
# Input:
#              9
#               \
#                10
#                 \
#                  11
# Output: 9
# Your Task:
# The task is to complete the function minValue() which takes root as the argument and returns the minimum element of BST. If the tree is empty, there is no minimum element, so return -1 in that case.

# Expected Time Complexity: O(Height of the BST)
# Expected Auxiliary Space: O(1).


class Solution:
    # Function to find the minimum element in the given BST.
    def minValue(self, root):
        ##Your code here
        return root.data if root.left == None else Solution().minValue(root.left)


from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
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


if __name__ == "__main__":
    s = input()
    root = buildTree(s)
    ob = Solution()
    print(ob.minValue(root))
