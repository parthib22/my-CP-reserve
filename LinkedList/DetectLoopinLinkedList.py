# https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1

# Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

# Example 1:
# Input:
# N = 3
# value[] = {1,3,4}
# x(position at which tail is connected) = 2
# Output: True
# Explanation: In above test case N = 3.
# The linked list with nodes N = 3 is
# given. Then value of x=2 is given which
# means last node is connected with xth
# node of linked list. Therefore, there
# exists a loop.

# Example 2:
# Input:
# N = 4
# value[] = {1,8,3,4}
# x = 0
# Output: False
# Explanation: For N = 4 ,x = 0 means
# then lastNode->next = NULL, then
# the Linked list does not contains
# any loop.
# Your Task:
# The task is to complete the function detectloop() which contains reference to the head as only argument.  This function should return true if linked list contains loop, else return false.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)


class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # code here

        visited = set()
        start = head

        while start:
            if start in visited:
                return True

            visited.add(start)
            start = start.next

        return False

    #  Floyd's Cycle Detection Algorithm

    # dub = head
    # slow = dub
    # fast = dub.next

    # while fast and fast.next:

    #     if(slow == fast):
    #         return True

    #     slow = slow.next
    #     fast = fast.next.next

    # return False


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
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    # connects last node to node at position pos from begining.
    def loopHere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == "__main__":
    n = int(input())

    LL = LinkedList()
    for i in input().split():
        LL.insert(int(i))

    LL.loopHere(int(input()))

    print(Solution().detectLoop(LL.head))
