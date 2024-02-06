# GFG POTD 05.02.2024

# Sorted insert for circular linked list

# Given a sorted circular linked list of length n, the task is to insert a new node in this circular list so that it remains a sorted circular linked list.

# Example 1:

# Input:
# n = 3
# LinkedList = 1->2->4
# (the first and last node is connected, i.e. 4 --> 1)
# data = 2
# Output:
# 1 2 2 4
# Explanation:
# We can add 2 after the second node.
# Example 2:

# Input:
# n = 4
# LinkedList = 1->4->7->9
# (the first and last node is connected, i.e. 9 --> 1)
# data = 5
# Output:
# 1 4 5 7 9
# Explanation:
# We can add 5 after the second node.
# Your Task:
# The task is to complete the function sortedInsert() which should insert the new node into the given circular linked list and return the head of the linked list.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)


class Solution:
    def sortedInsert(self, head, data):
        # code here
        new_node = Node(data)

        # Case 1: If the list is empty
        if head is None:
            new_node.next = new_node
            head = new_node

        # Case 2: If the new node is to be inserted before the head node
        elif data <= head.data:
            temp = head
            while temp.next != head:
                temp = temp.next
            temp.next = new_node
            new_node.next = head
            head = new_node

        # Case 3: If the new node is to be inserted somewhere after the head
        else:
            temp = head
            while temp.next != head and temp.next.data < data:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

        return head


# Driver Code Starts
# contributed by RavinderSinghPB
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.last = None

    # Function to insert a new node
    def push(self, data):
        if not self.head:
            nn = Node(data)
            self.head = nn
            self.last = nn
            nn.next = nn
            return
        nn = Node(data)
        nn.next = self.head
        self.last.next = nn
        self.last = nn


# Utility function to print the linked LinkedList


def printList(head):
    if not head:
        return
    temp = head
    print(temp.data, end=" ")
    temp = temp.next
    while temp != head:
        print(temp.data, end=" ")
        temp = temp.next


if __name__ == "__main__":
    # t = int(input())
    # for tcs in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    data = int(input())

    cll = LinkedList()
    for e in arr:
        cll.push(e)

    reshead = Solution().sortedInsert(cll.head, data)
    printList(reshead)
    print()
