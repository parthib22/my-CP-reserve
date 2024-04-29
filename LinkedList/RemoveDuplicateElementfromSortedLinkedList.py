# https://www.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1

# Remove duplicate element from sorted Linked List

# Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).
# Note: Try not to use extra space. The nodes are arranged in a sorted way.

# Example 1:
# Input:
# LinkedList: 2->2->4->5
# Output: 2 4 5
# Explanation: In the given linked list
# 2 ->2 -> 4-> 5, only 2 occurs more
# than 1 time. So we need to remove it once.

# Example 2:
# Input:
# LinkedList: 2->2->2->2->2
# Output: 2
# Explanation: In the given linked list
# 2 ->2 ->2 ->2 ->2, 2 is the only element
# and is repeated 5 times. So we need to remove
# any four 2.
# Your Task:
# The task is to complete the function removeDuplicates() which takes the head of input linked list as input. The function should remove the duplicates from linked list and return the head of the linkedlist.

# Expected Time Complexity : O(N)
# Expected Auxilliary Space : O(1)


def removeDuplicates(head):
    # code here

    start = head

    # n = None

    # while start:
    #     if start.data != n:
    #         n = start.data
    #         temp = start
    #     else:
    #         temp.next = start.next

    #     start = start.next

    while start:
        if start.next and start.next.data == start.data:
            start.next = start.next.next
        else:
            start = start.next

    return head


import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the
    # linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self):
        if self.head is None:
            print(" ")
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print("")


if __name__ == "__main__":
    n = int(input())
    a = LinkedList()  # create a new linked list 'a'.
    nodes = list(map(int, input().strip().split()))
    for x in nodes:
        a.append(x)
    removeDuplicates(a.head)
    a.printList()
