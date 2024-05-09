# https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1

# Rotate a Linked List

# Given a singly linked list of size N. The task is to left-shift the linked list by k nodes, where k is a given positive integer smaller than or equal to length of the linked list.

# Example 1:
# Input:
# N = 5
# value[] = {2, 4, 7, 8, 9}
# k = 3
# Output: 8 9 2 4 7
# Explanation:
# Rotate 1: 4 -> 7 -> 8 -> 9 -> 2
# Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
# Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

# Example 2:
# Input:
# N = 8
# value[] = {1, 2, 3, 4, 5, 6, 7, 8}
# k = 4
# Output: 5 6 7 8 1 2 3 4

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function rotate() which takes a head reference as the first argument and k as the second argument, and returns the head of the rotated linked list.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).


class Solution:

    # Function to rotate a linked list.
    def rotate(self, head, k):
        # code here

        if k == 0:
            return head
        size = 0
        start = head
        while start:
            size = size + 1
            end = start
            start = start.next
        k = k % size
        if k == 0:
            return head

        while k > 0:
            beg = head
            head = head.next
            end.next = beg
            beg.next = None
            end = end.next
            k -= 1

        return head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(n):
    while n:
        print(n.data, end=" ")
        n = n.next
    print()


if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    k = int(input())

    lis = LinkedList()
    for i in arr:
        lis.insert(i)

    head = Solution().rotate(lis.head, k)
    printList(head)
