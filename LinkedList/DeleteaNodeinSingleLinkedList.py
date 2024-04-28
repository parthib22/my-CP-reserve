# https://www.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1

# Delete a Node in Single Linked List

# Given a singly linked list and an integer x.Delete xth node from the singly linked list.

# Example 1:
# Input: 1 -> 3 -> 4
#        x = 3
# Output: 1 -> 3
# Explanation:
# After deleting the node at 3rd
# position (1-base indexing), the
# linked list is as 1 -> 3.

# Example 2:
# Input: 1 -> 5 -> 2 -> 9
# x = 2
# Output: 1 -> 2 -> 9
# Explanation:
# After deleting the node at 2nd
# position (1-based indexing), the
# linked list is as 1 -> 2 -> 9.
# Your task: Your task is to complete the method deleteNode() which takes two arguments: the address of the head of the linked list and an integer x. The function returns the head of the modified linked list.


def delNode(head, k):
    # Code here

    if k == 1:
        return head.next

    start = head

    while k > 2:
        start = start.next
        k -= 1

    start.next = start.next.next if start.next.next else None

    return head


class node:
    def __init__(self):
        self.data = None
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
            self.last = self.head
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.last.next = new_node
            self.last = new_node
            # self.
            # temp = self.head
            # while(temp.next):
            #     temp=temp.next
            # temp.next = new_node


def printlist(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print("")


# Driver Program
if __name__ == "__main__":
    list1 = Linked_List()
    n = int(input())
    values = list(map(int, input().strip().split()))
    for i in values:
        list1.insert(i)
    k = int(input())
    newhead = delNode(list1.head, k)
    printlist(newhead)
