# https://www.geeksforgeeks.org/problems/k-distance-from-root/1

# POTD 03.05.2024

# K distance from root

# Given a binary tree having n nodes and an integer k. Print all nodes that are at distance k from the root (root is considered at distance 0 from itself). Nodes should be printed from left to right.

# Example 1:
# Input:
# k = 0
#       1
#     /   \
#    3     2
# Output:
# 1
# Explanation:
# 1 is the only node which is 0 distance from the root 1.
# Example 2:

# Input:
# k = 3
#         1
#        /
#       2
#        \
#         1
#       /  \
#      5    3
# Output:
# 5 3
# Explanation:
# 5 and 3 are the nodes which are at distance 3 from the root 3.
# Here, returning 3 5 will be incorrect.
# Your Task:
# You don't have to take input. Complete the function Kdistance() that accepts root node and k as parameters and returns the value of the nodes that are at a distance k from the root.

# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(Height of the Tree).


class Solution:
    def KDistance(self, root, k):
        # code here
        if not root:
            return None

        q = deque([(root, 0)])
        ans = []

        while q:

            # print(q[0].data, end = " ")
            node, dist = q.popleft()

            if dist == k:
                ans.append(node.data)

            if node.left:
                q.append((node.left, dist + 1))

            if node.right:
                q.append((node.right, dist + 1))

        return ans


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
    k = int(input())
    s = input()
    root = buildTree(s)
    ob = Solution()
    nodes = ob.KDistance(root, k)
    for node in nodes:
        print(node, end=" ")
