# https://www.geeksforgeeks.org/problems/count-pairs-whose-sum-is-equal-to-x/1

# POTD 17.03.2024

# Count Pairs whose sum is equal to X

# Given two linked list head1 and head2 with distinct elements, determine the count of all distinct pairs from both lists whose sum is equal to the given value x.

# Note: A valid pair would be in the form (x, y) where x is from first linked list and y is from second linked list.

# Example 1:
# Input:
# head1 = 1->2->3->4->5->6
# head2 = 11->12->13
# x = 15
# Output: 3
# Explanation: There are total 3 pairs whose sum is 15 : (4,11) , (3,12) and (2,13)

# Example 2:
# Input:
# head1 = 7->5->1->3
# head2 = 3->5->2->8
# x = 10
# Output: 2
# Explanation: There are total 2 pairs whose sum is 10 : (7,3) and (5,5)
# Your Task:
# You only need to implement the given function countPairs() that take two linked list head1 and head2 and return the count of distinct pairs whose sum is equal to x.

# Expected Time Complexity: O(length(head1)+lenght(head2)).
# Expected Auxiliary Space: O(length(head1)) or O(length(head2)).

# Constraints:
# 1<=length(head1), lenght(head2)<=105
# 1 <= Value of elements of  linked lists <= 109
# 1<= x <= 109
# Note : All elements in each linked list are unique.


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        """
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        """
        start = head1
        _set = set()
        while start != None:
            _set.add(start.data)
            start = start.next
        count = 0
        start = head2
        while start != None:
            if (x - start.data) in _set:
                count += 1
            start = start.next
        return count


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


if __name__ == "__main__":
    n1 = int(input())
    ll1 = LinkedList()  # create a new linked list 'll1'.
    nodes_ll1 = list(map(int, input().strip().split()))
    for nodes in nodes_ll1:
        ll1.append(nodes)  # add to the end of the list

    n2 = int(input())
    ll2 = LinkedList()  # create a new linked list 'll1'.
    nodes_ll2 = list(map(int, input().strip().split()))
    for nodes in nodes_ll2:
        ll2.append(nodes)  # add to the end of the list

    x = int(input())

    print(Solution().countPair(ll1.head, ll2.head, n1, n2, x))
