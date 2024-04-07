# https://www.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1

# Sum of nodes on the longest path from root to leaf node

# Given a binary tree having n nodes. Find the sum of all nodes on the longest path from root to any leaf node. If two or more paths compete for the longest path, then the path having maximum sum of nodes will be considered.

# Example 1:
# Input:
#         4
#        / \
#       2   5
#      / \  /\
#     7  1 2  3
#       /
#      6
# Output:
# 13
# Explanation:
#         4
#        / \
#       2   5
#      / \  /\
#     7  1 2  3
#       /
#      6
# The highlighted nodes (4, 2, 1, 6) above are part of the longest root to leaf path having sum = (4 + 2 + 1 + 6) = 13

# Example 2:
# Input:
#           1
#         /  \
#        2    3
#       / \   /\
#      4   5 6  7
# Output:
# 11
# Explanation:
# Use path 1->3->7, with sum 11.
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function sumOfLongRootToLeafPath() which takes root node of the tree as input parameter and returns an integer denoting the sum of the longest root to leaf path of the tree.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)


class Solution:
    def sumOfLongRootToLeafPath(self, root):
        # code here
        sum = 0
        maxsum = -1
        len = 0
        maxlen = 0

        def solve(root, sum, maxsum, len, maxlen):
            if not root:
                if len > maxlen:
                    maxsum = sum
                    maxlen = len
                elif len == maxlen:
                    maxsum = max(sum, maxsum)
                return maxsum, maxlen
            maxsum, maxlen = solve(root.left, sum + root.data, maxsum, len + 1, maxlen)
            maxsum, maxlen = solve(root.right, sum + root.data, maxsum, len + 1, maxlen)
            return maxsum, maxlen

        maxsum, maxlen = solve(root, sum, maxsum, len, maxlen)
        return maxsum


from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


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
    res = ob.sumOfLongRootToLeafPath(root)
    print(res)
