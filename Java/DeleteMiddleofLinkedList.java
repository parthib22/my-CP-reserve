// https://www.geeksforgeeks.org/problems/delete-middle-of-linked-list/1

// Delete Middle of Linked List

// POTD 28.04.2024

// Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.
// If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.
// If the input linked list has single node, then it should return NULL.

// Example 1:
// Input:
// LinkedList: 1->2->3->4->5
// Output: 
// 1 2 4 5

// Example 2:
// Input:
// LinkedList: 2->4->6->7->5->1
// Output: 
// 2 4 6 5 1
// Your Task:
// The task is to complete the function deleteMid() which takes head of the linkedlist  and return head of the linkedlist with middle element deleted from the linked list. If the linked list is empty or contains single element then it should return NULL.

// Expected Time Complexity: O(n).
// Expected Auxiliary Space: O(1).

import java.util.*;
import java.io.*;

class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }

}

public class DeleteMiddleofLinkedList {
    static void printList(Node node) {
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
        System.out.println();
    }

    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Node head = new Node(sc.nextInt());
        Node tail = head;
        for (int i = 0; i < n - 1; i++) {
            tail.next = new Node(sc.nextInt());
            tail = tail.next;
        }
        Solution g = new Solution();
        head = g.deleteMid(head);
        printList(head);
        sc.close();
    }
}

class Solution {
    Node deleteMid(Node head) {
        // This is method only submission.
        // You only need to complete the method.
        if (head == null || head.next == null) {
            return null;
        }
        Node fast = head;
        Node slow = head;
        Node temp = null;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            temp = slow;
            slow = slow.next;
        }

        temp.next = temp.next.next;

        return head;
    }
}