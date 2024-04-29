# https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1

# Nth node from end of linked list

# Given a linked list consisting of L nodes and given a number N. The task is to find the Nth node from the end of the linked list.

# Example 1:
# Input:
# N = 2
# LinkedList: 1->2->3->4->5->6->7->8->9
# Output: 8
# Explanation: In the first example, there
# are 9 nodes in linked list and we need
# to find 2nd node from end. 2nd node
# from end is 8.

# Example 2:
# Input:
# N = 5
# LinkedList: 10->5->100->5
# Output: -1
# Explanation: In the second example, there
# are 4 nodes in the linked list and we
# need to find 5th from the end. Since 'n'
# is more than the number of nodes in the
# linked list, the output is -1.
# Your Task:
# The task is to complete the function getNthFromLast() which takes two arguments: reference to head and N and you need to return Nth from the end or -1 in case node doesn't exist.

# Note:
# Try to solve in a single traversal.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).


def getNthFromLast(head, n):
    # code here

    # start = head
    # pointer = 0

    # while start:
    #     pointer += 1
    #     start = start.next

    # pointer = pointer - n

    # start = head

    # while start and pointer > 0:
    #     pointer -= 1
    #     start = start.next

    # return -1 if not start or pointer < 0 else start.data

    start = head
    arr = []

    while start:
        arr.append(start.data)
        start = start.next

    if n < 1 or n > len(arr):
        return -1

    return arr[-n]


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

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


if __name__ == "__main__":
    n, nth_node = map(int, input().strip().split())
    a = LinkedList()  # create a new linked list 'a'.
    nodes_a = list(map(int, input().strip().split()))
    for x in nodes_a:
        a.append(x)  # add to the end of the list
    print(getNthFromLast(a.head, nth_node))
