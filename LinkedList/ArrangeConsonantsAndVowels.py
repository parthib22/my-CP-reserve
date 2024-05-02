# https://www.geeksforgeeks.org/problems/arrange-consonants-and-vowels/1

# POTD 01.05.2024

# Arrange Consonants and Vowels

# Given a singly linked list having n nodes containing english alphabets ('a'-'z'). Rearrange the linked list in such a way that all the vowels come before the consonants while maintaining the order of their arrival.

# Example 1:
# Input:
# n = 9
# linked list: a -> b -> c -> d -> e -> f -> g -> h -> i
# Output:
# a -> e -> i -> b -> c -> d -> f -> g -> h
# Explanation:
# After rearranging the input linked list according to the condition the resultant linked list will be as shown in output.

# Example 2:
# Input:
# n = 8
# linked list: a -> b -> a -> b -> d -> e -> e -> d
# Output:
# a -> a -> e -> e -> b -> b -> d -> d
# Explanation:
# After rearranging the input linked list according to the condition the resultant linked list will be as shown in output.
# Your Task:
# Your task is to complete the function arrangeCV(), which takes head of linked list and arranges the list in such a way that all the vowels come before the consonants while maintaining the order of their arrival and returns the head of the updated linked list.

# Expected Time Complexity :  O(n)
# Expected Auxiliary Space :  O(1)


class Solution:
    # Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here

        # vowels = ['a', 'e', 'i', 'o', 'u']
        # start = head
        # v = []
        # c = []

        # while start:
        #     if start.data in vowels:
        #         v.append(start.data)
        #     else:
        #         c.append(start.data)
        #     start = start.next

        # start = head

        # for _v in v:
        #     start.data = _v
        #     start = start.next

        # for _c in c:
        #     start.data = _c
        #     start = start.next

        # return head

        vowels = ["a", "e", "i", "o", "u"]

        v_dummy = Node(0)
        c_dummy = Node(0)
        v_temp = v_dummy
        c_temp = c_dummy

        start = head

        while start:

            if start.data in vowels:
                v_dummy.next = start
                v_dummy = v_dummy.next
            else:
                c_dummy.next = start
                c_dummy = c_dummy.next

            start = start.next

        c_dummy.next = None

        v_dummy.next = c_temp.next

        return v_temp.next


class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()


if __name__ == "__main__":

    n = int(input())
    arr = [str(x) for x in input().split()]

    lis = Linked_List()
    for i in arr:
        lis.insert(i)

    newHead = Solution().arrangeCV(lis.head)
    printList(newHead)
