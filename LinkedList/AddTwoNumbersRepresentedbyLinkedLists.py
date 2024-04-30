# https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1

# POTD 30.04.2024

# Add two numbers represented by linked lists

# Given two decimal numbers, num1 and num2, represented by linked lists of size n and m respectively. The task is to return a linked list that represents the sum of these two numbers.

# For example, the number 190 will be represented by the linked list, 1->9->0->null, similarly 25 by 2->5->null. Sum of these two numbers is 190 + 25 = 215, which will be represented by 2->1->5->null. You are required to return the head of the linked list 2->1->5->null.

# Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

# Example 1:
# Input:
# n = 2
# num1 = 45 (4->5->null)
# m = 3
# num2 = 345 (3->4->5->null)
# Output:
# 3->9->0->null
# Explanation:
# For the given two linked list (4 5) and (3 4 5), after adding the two linked list resultant linked list will be (3 9 0).

# Example 2:
# Input:
# n = 4
# num1 = 0063 (0->0->6->3->null)
# m = 2
# num2 = 07 (0->7->null)
# Output:
# 7->0->null
# Explanation:
# For the given two linked list (0 0 6 3) and (0 7), after adding the two linked list resultant linked list will be (7 0).
# Your Task:
# The task is to complete the function addTwoLists() which has node reference of both the linked lists and returns the head of the sum list.

# Expected Time Complexity: O(n+m)
# Expected Auxiliary Space: O(max(n,m)) for the resultant list.


class Solution:
    # Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        # code here
        # return head of sum list
        def helper(num):
            s = ""
            while num:
                s += str(num.data)
                num = num.next
            return int(s)

        res = str(helper(num1) + helper(num2))

        head = start = Node(res[0])
        for r in res[1:]:
            start.next = Node(r)
            start = start.next

        return head


# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=" ")
        n = n.next
    print()


if __name__ == "__main__":
    n = int(input())
    arr1 = (int(x) for x in input().split())
    num1 = LinkedList()
    for i in arr1:
        num1.insert(i)

    m = int(input())
    arr2 = (int(x) for x in input().split())
    num2 = LinkedList()
    for i in arr2:
        num2.insert(i)

    res = Solution().addTwoLists(num1.head, num2.head)
    printList(res)
