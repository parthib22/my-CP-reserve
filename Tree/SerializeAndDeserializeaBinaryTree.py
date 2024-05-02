# https://www.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1

# POTD 02.05.2024

# Serialize and deserialize a binary tree

# Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions

# serialize() : stores the tree into an array a and returns the array.
# deSerialize() : deserializes the array to the tree and returns the root of the tree.
# Note: Multiple nodes can have the same data and the node values are always positive integers. Your code will be correct if the tree returned by deSerialize(serialize(input_tree)) is same as the input tree. Driver code will print the in-order traversal of the tree returned by deSerialize(serialize(input_tree)).

# Example 1:
# Input:
#       1
#     /   \
#    2     3
# Output:
# 2 1 3

# Example 2:
# Input:
#          10
#        /    \
#       20    30
#     /   \
#    40  60
# Output:
# 40 20 60 10 30
# Your Task:
# The task is to complete two functions serialize which takes the root node of the tree as input and stores the tree into an array and deSerialize which deserializes the array to the original tree and returns the root of it.

# Expected Time Complexity: O(Number of nodes).
# Expected Auxiliary Space: O(Number of nodes).


class Solution:
    # Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        # code here
        a = []

        def inorder(root):
            nonlocal a
            if not root:
                return

            inorder(root.left)
            a.append(root.data)
            inorder(root.right)

        inorder(root)

        return a

    # Function to deserialize a list and construct the tree.
    def deSerialize(self, a):
        # code here

        def helper(a, left, right):

            if left > right:
                return

            idx = (left + right) // 2

            root = Node(a[idx])
            root.left = helper(a, left, idx - 1)
            root.right = helper(a, idx + 1, right)

            return root

        return helper(a, 0, len(a) - 1)


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


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def _deleteTree(node):
    if node == None:
        return

    # first delete both subtrees
    _deleteTree(node.left)
    _deleteTree(node.right)
    node.left = None
    node.right = None
    # then delete the node


# Deletes a tree and sets the root as NULL
def deleteTree(node_ref):
    _deleteTree(node_ref)
    node_ref = None


if __name__ == "__main__":
    root = buildTree(input())
    ob = Solution()
    A = ob.serialize(root)
    deleteTree(root)
    root = None
    r = ob.deSerialize(A)
    inorder(r)
