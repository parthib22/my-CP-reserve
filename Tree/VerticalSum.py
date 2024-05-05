# https://www.geeksforgeeks.org/problems/vertical-sum/1

# POTD 05.05.2024

# Vertical sum

# Given a binary tree having n nodes, find the vertical sum of the nodes that are in the same vertical line. Return all sums through different vertical lines starting from the left-most vertical line to the right-most vertical line.

# Example 1:
# Input:
#        1
#     /    \
#   2      3
#  /  \    /  \
# 4   5  6   7
# Output:
# 4 2 12 3 7
# Explanation:
# The tree has 5 vertical lines
# Line 1 has only one node 4 => vertical sum is 4.
# Line 2 has only one node 2 => vertical sum is 2.
# Line-3 has three nodes: 1,5,6 => vertical sum is 1+5+6 = 12.
# Line-4 has only one node 3 => vertical sum is 3.
# Line-5 has only one node 7 => vertical sum is 7.

# Example 2:
# Input:
#           1
#          /
#         2
#        /
#       3
#      /
#     4
#    /
#   6
#  /
# 7
# Output:
# 7 6 5 4 3 2 1
# Explanation:
# There are seven vertical lines each having one node.
# Your Task:
# You don't need to take input. Just complete the function verticalSum() that takes root node of the tree as parameter and returns an array containing the vertical sum of tree from left to right.

# Expected Time Complexity: O(nlogn).
# Expected Auxiliary Space: O(n).


class Solution:
    # Complete the function below
    def verticalSum(self, root):
        #:param root: root of the given tree.
        # code here
        mapp = {}

        def dfs(node, pos):
            if not node:
                return
            dfs(node.left, pos - 1)
            mapp[pos] = mapp.get(pos, 0) + node.data
            dfs(node.right, pos + 1)

        dfs(root, 0)

        return [val for _, val in sorted(mapp.items())]
        # return mapp.values() # this didnot work during submit, so we did the above---


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
    res = Solution().verticalSum(root)
    for i in res:
        print(i, end=" ")
