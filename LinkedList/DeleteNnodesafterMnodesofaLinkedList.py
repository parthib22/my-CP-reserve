# https://www.geeksforgeeks.org/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/1

# Delete N nodes after M nodes of a linked list

# Given a linked list, delete N nodes after skipping M nodes of a linked list until the last of the linked list.

# Example:
# Input:
# 2
# 8
# 2 1
# 9 1 3 5 9 4 10 1
# 6
# 6 1
# 1 2 3 4 5 6

# Output:
# 9 1 5 9 10 1
# 1 2 3 4 5 6

# Explanation:
# Deleting one node after skipping the M nodes each time, we have list as 9-> 1-> 5-> 9-> 10-> 1.
# Input:
# The first line of input contains the number of test cases T. For each test case, the first line of input contains a number of elements in the linked list, and the next M and N respectively space-separated. The last line contains the elements of the linked list.

# Output:
# The function should not print any output to the stdin/console.

# Your Task:
# The task is to complete the function linkdelete() which should modify the linked list as required.


class Solution:
    def skipMdeleteN(self, head, M, N):
        # Code here

        start = head

        while True:

            for _ in range(M):
                if not start:
                    return head
                prev = start
                start = start.next

            for _ in range(N):
                if not start:
                    return head
                start = start.next
                prev.next = start


class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("")


if __name__ == "__main__":
    llist = LinkedList()
    n = int(input())
    m, p = list(map(int, input().strip().split()))
    values = input().strip().split()
    for i in reversed(values):
        llist.push(i)
    Solution().skipMdeleteN(llist.head, m, p)
    llist.printList()
