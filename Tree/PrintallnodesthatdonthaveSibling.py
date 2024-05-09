# https://www.geeksforgeeks.org/problems/print-all-nodes-that-dont-have-sibling/1

# POTD 06.05.2024

# Print all nodes that don't have sibling

# Given a Binary Tree of n nodes, find all the nodes that don't have any siblings. You need to return a list of integers containing all the nodes that don't have a sibling in sorted order (Increasing).

# Two nodes are said to be siblings if they are present at the same level, and their parents are the same.

# Note: The root node can not have a sibling so it cannot be included in our answer.

# Example 1:
# Input :
#        37
#       /
#     20
#     /
#   113

# Output:
# 20 113
# Explanation:
# Nodes 20 and 113 dont have any siblings.

# Example 2:
# Input :
#        1
#       / \
#      2   3

# Output:
# -1
# Explanation:
# Every node has a sibling.
# Your Task:
# You don't need to read input or print anything. Complete the function noSibling() which takes the root of the tree as input parameter and returns a list of integers containing all the nodes that don't have a sibling in sorted order. If all nodes have a sibling, then the returning list should contain only one element -1.

# Expected Time Complexity: O(nlogn)
# Expected Auxiliary Space: O(Height of the tree)


def noSibling(root):
    # code here
    ans = []

    def dfs(root):
        if not root:
            return

        if root.left and not root.right:
            ans.append(root.left.data)
        elif root.right and not root.left:
            ans.append(root.right.data)

        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return sorted(ans) if ans else [-1]


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
    #   print(ip)
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
    ans = noSibling(root)
    for i in ans:
        print(i, end=" ")
