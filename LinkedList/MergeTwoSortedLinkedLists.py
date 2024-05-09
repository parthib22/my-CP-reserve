# https://www.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1

# Merge two sorted linked lists

# Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.

# Example 1:
# Input:
# N = 4, M = 3
# valueN[] = {5,10,15,40}
# valueM[] = {2,3,20}
# Output: 2 3 5 10 15 20 40
# Explanation: After merging the two linked
# lists, we have merged list as 2, 3, 5,
# 10, 15, 20, 40.

# Example 2:
# Input:
# N = 2, M = 2
# valueN[] = {1,1}
# valueM[] = {2,4}
# Output:1 1 2 4
# Explanation: After merging the given two
# linked list , we have 1, 1, 2, 4 as
# output.
# Your Task:
# The task is to complete the function sortedMerge() which takes references to the heads of two linked lists as the arguments and returns the head of merged linked list.

# Expected Time Complexity : O(n+m)
# Expected Auxilliary Space : O(1)


def sortedMerge(head1, head2):
    # code here
    if head1.data > head2.data:
        large, small = head1, head2
    else:
        large, small = head2, head1

    merge = prev = small

    while large:

        while small and small.data <= large.data:
            prev, small = small, small.next

        prev.next = large
        nxt = large.next
        large.next = small
        small, large = large, nxt

        if not small:
            break

    return merge


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


# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=" ")
        n = n.next
    print()


if __name__ == "__main__":
    n, m = map(int, input().strip().split())

    a = LinkedList()  # create a new linked list 'a'.
    b = LinkedList()  # create a new linked list 'b'.

    nodes_a = list(map(int, input().strip().split()))
    nodes_b = list(map(int, input().strip().split()))

    for x in nodes_a:
        a.append(x)

    for x in nodes_b:
        b.append(x)

    printList(sortedMerge(a.head, b.head))
