# https://www.geeksforgeeks.org/problems/closest-neighbor-in-bst/1

# Closest Neighbour in BST

# Given the root of a binary search tree and a number n, find the greatest number in the binary search tree that is less than or equal to n.

# Example 1 :
# Input : http://contribute.geeksforgeeks.org/wp-content/uploads/g.png

# n = 24
# Output :
# 21
# Explanation : The greatest element in the tree which
#               is less than or equal to 24, is 21.
#               (Searching will be like 5->12->21)

# Example 2 :
# Input : http://contribute.geeksforgeeks.org/wp-content/uploads/g.png

# n = 4
# Output :
# 3
# Explanation : The greatest element in the tree which
#               is less than or equal to 4, is 3.
#               (Searching will be like 5->2->3)
# Your task :
# You don't need to read input or print anything. Your task is to complete the function findMaxForN() which takes the root of the BST, and the integer n as input parameters and returns the greatest element less than or equal to n in the given BST, Return -1 if no such element exists.

# Expected Time Complexity: O(Height of the BST)
# Expected Auxiliary Space: O(Height of the BST).


class Solution:
    def findMaxForN(self, root, n):
        def inorder(node, current_max):
            if node is None:
                return current_max

            current_max = inorder(node.left, current_max)

            if node.key <= n:
                current_max = max(current_max, node.key)

            current_max = inorder(node.right, current_max)

            return current_max

        max_value = inorder(root, -1)
        return max_value


from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.key = val
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
    n = int(input())
    ob = Solution()
    print(ob.findMaxForN(root, n))
