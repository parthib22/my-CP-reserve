# https://www.geeksforgeeks.org/problems/delete-middle-of-linked-list/1

# POTD 28.04.2024

# Delete Middle of Linked List

# Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.
# If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.
# If the input linked list has single node, then it should return NULL.

# Example 1:
# Input:
# LinkedList: 1->2->3->4->5
# Output:
# 1 2 4 5

# Example 2:
# Input:
# LinkedList: 2->4->6->7->5->1
# Output:
# 2 4 6 5 1
# Your Task:
# The task is to complete the function deleteMid() which takes head of the linkedlist  and return head of the linkedlist with middle element deleted from the linked list. If the linked list is empty or contains single element then it should return NULL.

# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(1).


class Solution:
    def deleteMid(self, head):
        """
        head:  head of given linkedList
        return: head of resultant llist
        """

        # code here

        if not head or not head.next:
            return None

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            mid = slow
            slow = slow.next

        mid.next = mid.next.next

        return head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    n = int(input())
    arr1 = [int(x) for x in input().split()]
    ll = Llist()
    tail = None
    for nodeData in arr1:
        tail = ll.insert(nodeData, tail)
    obj = Solution()
    res = obj.deleteMid(ll.head)
    printList(res)
