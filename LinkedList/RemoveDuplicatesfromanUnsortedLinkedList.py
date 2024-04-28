# https://www.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1

# Remove duplicates from an unsorted linked list

# Given an unsorted linked list of N nodes. The task is to remove duplicate elements from this unsorted Linked List. When a value appears in multiple nodes, the node which appeared first should be kept, all others duplicates are to be removed.

# Example 1:
# Input:
# N = 4
# value[] = {5,2,2,4}
# Output: 5 2 4
# Explanation:Given linked list elements are
# 5->2->2->4, in which 2 is repeated only.
# So, we will delete the extra repeated
# elements 2 from the linked list and the
# resultant linked list will contain 5->2->4

# Example 2:
# Input:
# N = 5
# value[] = {2,2,2,2,2}
# Output: 2
# Explanation:Given linked list elements are
# 2->2->2->2->2, in which 2 is repeated. So,
# we will delete the extra repeated elements
# 2 from the linked list and the resultant
# linked list will contain only 2.
# Your Task:
# You have to complete the method removeDuplicates() which takes 1 argument: the head of the linked list.  Your function should return a pointer to a linked list with no duplicate element.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)


class Solution:
    # Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list

        visited = set()

        start = head

        while start:
            if start.data in visited:
                temp.next = start.next
            else:
                visited.add(start.data)
                temp = start

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

    # creates a new node with given value and appends it at the end of the linked list
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
        print(" ")


if __name__ == "__main__":
    n = int(input())
    a = LinkedList()  # create a new linked list 'a'.
    nodes = list(map(int, input().strip().split()))
    for x in nodes:
        a.append(x)
    a.head = Solution().removeDuplicates(a.head)
    a.printList()
