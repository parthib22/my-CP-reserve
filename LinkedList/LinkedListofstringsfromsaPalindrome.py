# https://www.geeksforgeeks.org/problems/linked-list-of-strings-forms-a-palindrome/1

# POTD 02.07.2024

# Linked list of strings forms a palindrome

# Given a linked list with string data, check whether the combined string formed is palindrome. If the combined string is palindrome then return true otherwise return false.

# Example:

# Input:
# https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700056/Web/Other/blobid0_1719813534.png
# Output : true
# Explanation: As string "abcddcba" is palindrome the function should return true.

# Input:
# https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700056/Web/Other/blobid1_1719813588.png
# Output : false
# Explanation: As string "abcdba" is not palindrome the function should return false.
# Expected Time Complexity:  O(n)
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 <= Node.data.length<= 10^3
# 1<=list.length<=10^3


def compute(head):
    # return True/False
    s = ""

    start = head
    while start:
        s += start.data
        start = start.next

    return s == s[::-1]


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


if __name__ == "__main__":

    n1 = int(input())
    arr1 = input().split()
    ll1 = Llist()
    tail = None
    for nodeData in arr1:
        tail = ll1.insert(nodeData, tail)

    if compute(ll1.head):
        print("true")
    else:
        print("false")
