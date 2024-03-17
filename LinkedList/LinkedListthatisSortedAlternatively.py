# https://www.geeksforgeeks.org/problems/linked-list-that-is-sorted-alternatingly/1

# POTD 15.03.2024

# Linked List that is Sorted Alternatingly

# You are given a Linked list of size n. The list is in alternating ascending and descending orders. Sort the given linked list in non-decreasing order.

# Example 1:
# Input:
# n = 6
# LinkedList = 1->9->2->8->3->7
# Output: 1 2 3 7 8 9
# Explanation:
# After sorting the given list will be 1->2->3->7->8->9.

# Example 2:
# Input:
# n = 5
# LinkedList = 13->99->21->80->50
# Output: 13 21 50 80 99
# Explanation:
# After sorting the given list will be 13->21->50->80->99.
# Your Task:
# You do not need to read input or print anything. The task is to complete the function sort() which should sort the linked list of size n in non-decreasing order.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def sort(self, head):
        temp = list()
        start = head
        while start != None:
            temp.append(start.data)
            start = start.next
        temp.sort()
        start = head
        i = 0
        while start != None:
            start.data = temp[i]
            start = start.next
            i = i + 1
        return head


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


if __name__ == "__main__":
    n1 = int(input())
    arr1 = [int(x) for x in input().split()]
    ll1 = Llist()
    tail = None
    for nodeData in arr1:
        tail = ll1.insert(nodeData, tail)

    ob = Solution()
    resHead = ob.sort(ll1.head)
    printList(resHead)
    print()
