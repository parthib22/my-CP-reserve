# https://www.geeksforgeeks.org/problems/merge-sort-on-doubly-linked-list/1

# POTD 27.04.2024

# Merge Sort on Doubly Linked List

# Given Pointer/Reference to the head of a doubly linked list of n nodes, the task is to Sort the given doubly linked list using Merge Sort in both non-decreasing and non-increasing order.

# Example 1:
# Input:
# n = 8
# value[] = {7,3,5,2,6,4,1,8}
# Output:
# 1 2 3 4 5 6 7 8
# 8 7 6 5 4 3 2 1
# Explanation: After sorting the given
# linked list in both ways, resultant
# matrix will be as given in the first
# two line of output, where first line
# is the output for non-decreasing
# order and next line is for non-
# increasing order.

# Example 2:
# Input:
# n = 5
# value[] = {9,15,0,-1,0}
# Output:
# -1 0 0 9 15
# 15 9 0 0 -1
# Explanation: After sorting the given
# linked list in both ways, the
# resultant list will be -1 0 0 9 15
# in non-decreasing order and
# 15 9 0 0 -1 in non-increasing order.
# Your Task:
# The task is to complete the function sortDoubly() which takes reference to the head of the doubly linked and Sort the given doubly linked list using Merge Sort in both non-decreasing and non-increasing. The printing is done automatically by the driver code.

# Expected Time Complexity: O(nlogn)
# Expected Space Complexity: O(logn)


class Solution:
    # Function to sort the given doubly linked list using Merge Sort.
    def sortDoubly(self, head):
        # Your code here

        _list = []

        start = head
        while start:
            _list.append(start.data)
            temp = start
            start = start.next

        _list.sort()

        while temp:
            temp.data = _list.pop()
            temp = temp.prev

        return head

    def sortDoublyMerge(self, head):
        tail = head
        while tail.next:
            tail = tail.next

        def merge(head, mid, tail):
            temp = []
            i, j = head, mid.next
            while i != mid.next and j != tail.next:
                if i.data < j.data:
                    temp.append(i.data)
                    i = i.next
                else:
                    temp.append(j.data)
                    j = j.next
            if i != mid.next:
                while i != mid.next:
                    temp.append(i.data)
                    i = i.next
            if j != tail.next:
                while j != tail.next:
                    temp.append(j.data)
                    j = j.next
            k = head
            for i in temp:
                k.data = i
                k = k.next

        def mergesort(head, tail):
            if head != tail:
                temp, mid = head, head
                while temp != tail and temp.next != tail:
                    temp = temp.next.next
                    mid = mid.next
                mergesort(head, mid)
                mergesort(mid.next, tail)
                merge(head, mid, tail)

        mergesort(head, tail)
        return head


import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while node.next is not None:
            node = node.next
        while node.prev is not None:
            node = node.prev
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while node is not None:
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while temp:
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    llist = DoublyLinkedList()
    for e in arr:
        llist.append(e)
    ob = Solution()
    llist.head = ob.sortDoublyMerge(llist.head)
    printList(llist.head)
    print()
