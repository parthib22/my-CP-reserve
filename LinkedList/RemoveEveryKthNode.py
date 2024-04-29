# https://www.geeksforgeeks.org/problems/remove-every-kth-node/1

# Remove every kth node

# Given a singly linked list having n nodes, your task is to remove every kth node from the linked list.

# Example 1:
# Input:
# n = 8
# linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
# k = 2
# Output:
# 1 -> 3 -> 5 -> 7
# Explanation:
# After removing every 2nd node of the linked list, the resultant linked list will be: 1 -> 3 -> 5 -> 7.

# Example 2:
# Input:
# n = 10
# linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
# k = 3
# Output:
# 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
# Explanation:
# After removing every 3rd node of the linked list, the resultant linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.
# Your Task:
# The task is to complete the function deleteK() which takes head of linked list and integer k as input parameters and delete every kth node from the linked list and return its head.

# Expected Time Complexity :  O(n)
# Expected Auxiliary Space :  O(1)


class Solution:
    def deleteK(self, head, k):
        # code here

        if k == 1:
            return None
        
        start = head
        
        count = 1
        
        while start.next:
            count += 1
            if count % k == 0:
                start.next = start.next.next
            else:
                start = start.next
            
        return head

        # start = temp = head

        # while start:
        #     for _ in range(1, k):
        #         temp = start
        #         start = start.next
        #         if not start:
        #             return head

        #     temp.next = start.next
        #     start = start.next

        # return head


class node:

    def __init__(self, x):
        self.data = x
        self.next = None


def createLinkedList(arr):
    head = node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = node(arr[i])
        curr.next = new_node
        curr = curr.next

    return head


def printlist(ptr):
    while ptr != None:
        print(ptr.data, end=" ")
        ptr = ptr.next
    print()


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())

    obj = Solution()
    head = createLinkedList(arr)
    new_head = obj.deleteK(head, k)
    printlist(new_head)
