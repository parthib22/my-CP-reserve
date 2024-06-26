# https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1

# Flattening a Linked List

# Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
# (i) a next pointer to the next node,
# (ii) a bottom pointer to a linked list where this node is head.
# Each of the sub-linked-list is in sorted order.
# Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order.

# Note: The flattened list will be printed using the bottom pointer instead of the next pointer.
# For more clarity have a look at the printList() function in the driver code.

# Example 1:
# Input:
# 5 -> 10 -> 19 -> 28
# |     |     |     |
# 7     20    22   35
# |           |     |
# 8          50    40
# |                 |
# 30               45
# Output:  5-> 7-> 8- > 10 -> 19-> 20->
# 22-> 28-> 30-> 35-> 40-> 45-> 50.
# Explanation:
# The resultant linked lists has every
# node in a single level.
# (Note: | represents the bottom pointer.)

# Example 2:
# Input:
# 5 -> 10 -> 19 -> 28
# |          |
# 7          22
# |          |
# 8          50
# |
# 30
# Output: 5->7->8->10->19->22->28->30->50
# Explanation:
# The resultant linked lists has every
# node in a single level.

# (Note: | represents the bottom pointer.)

# Your Task:
# You do not need to read input or print anything. Complete the function flatten() that takes the head of the linked list as input parameter and returns the head of flattened link list.

# Expected Time Complexity: O(N*N*M)
# Expected Auxiliary Space: O(N)


def flatten(root):
    # Your code here
    start = btm = head
    a = []

    while start:
        a.append(start.data)
        btm = start.bottom
        while btm and btm.bottom:
            a.append(btm.data)
            btm = btm.bottom
        a.append(btm.data)
        btm.bottom = start.next
        start = start.next

    a.sort(reverse=True)

    start = head
    while start:
        start.data = a.pop()
        start = start.bottom

    return head


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.bottom

    print()


if __name__ == "__main__":

    head = None
    N = int(input())
    arr = []

    arr = [int(x) for x in input().strip().split()]
    temp = None
    tempB = None
    pre = None
    preB = None

    flag = 1
    flag1 = 1
    listo = [int(x) for x in input().strip().split()]
    it = 0
    for i in range(N):
        m = arr[i]
        m -= 1
        a1 = listo[it]
        it += 1
        temp = Node(a1)
        if flag == 1:
            head = temp
            pre = temp
            flag = 0
            flag1 = 1
        else:
            pre.next = temp
            pre = temp
            flag1 = 1

        for j in range(m):
            a = listo[it]
            it += 1
            tempB = Node(a)
            if flag1 == 1:
                temp.bottom = tempB
                preB = tempB
                flag1 = 0
            else:
                preB.bottom = tempB
                preB = tempB
    root = flatten(head)
    printList(root)
