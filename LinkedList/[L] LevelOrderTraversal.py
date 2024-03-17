# https://www.geeksforgeeks.org/problems/level-order-traversal/1

# POTD 18.03.2024

# Level order traversal

# Given a root of a binary tree with n nodes, find its level order traversal.
# Level order traversal of a tree is breadth-first traversal for the tree.

# Example 1:
# Input:
#     1
#   /   \
#  3     2
# Output:
# 1 3 2

# Example 2:
# Input:
#         10
#      /      \
#     20       30
#   /   \
#  40   60
# Output:
# 10 20 30 40 60
# Your Task:
# You don't have to take any input. Complete the function levelOrder() that takes the root node as input parameter and returns a list of integers containing the level order traversal of the given Binary Tree.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)


class Solution:
    # Function to return the level order traversal of a tree.
    def levelOrder(self, root):
        # Code here
        queue = []
        _list = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            _list.append(node.data)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return _list


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
    res = Solution().levelOrder(root)
    for i in res:
        print(i, end=" ")
    print()
