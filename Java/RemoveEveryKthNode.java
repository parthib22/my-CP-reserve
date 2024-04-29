// https://www.geeksforgeeks.org/problems/remove-every-kth-node/1

// Remove every kth node

// POTD 29.04.2024

// Given a singly linked list having n nodes, your task is to remove every kth node from the linked list. 

// Example 1:
// Input:
// n = 8
// linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 
// k = 2
// Output: 
// 1 -> 3 -> 5 -> 7
// Explanation: 
// After removing every 2nd node of the linked list, the resultant linked list will be: 1 -> 3 -> 5 -> 7.

// Example 2:
// Input:
// n = 10
// linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 
// k = 3
// Output: 
// 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10
// Explanation: 
// After removing every 3rd node of the linked list, the resultant linked list will be: 1 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10.
// Your Task:
// The task is to complete the function deleteK() which takes head of linked list and integer k as input parameters and delete every kth node from the linked list and return its head.

// Expected Time Complexity :  O(n)
// Expected Auxiliary Space :  O(1)

import java.util.*;

class Node {
    Node next;
    int data;

    Node(int d) {
        data = d;
        next = null;
    }
}

public class RemoveEveryKthNode {
    Node head;
    Node tail;

    void addToTheLast(Node node) {
        if (head == null) {
            head = node;
            tail = node;
        } else {
            tail.next = node;
            tail = tail.next;
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        RemoveEveryKthNode list = new RemoveEveryKthNode();
        // int n=Integer.parseInt(br.readLine());
        int a1 = sc.nextInt();
        Node head = new Node(a1);
        list.addToTheLast(head);
        for (int i = 1; i < n; i++) {
            int a = sc.nextInt();
            list.addToTheLast(new Node(a));
        }
        int k = sc.nextInt();
        // System.out.println(list.head.data+" "+ k);
        list.head = new Solution().delete(list.head, k);
        Node temp = list.head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
        sc.close();
    }
}

class Solution {
    /* You are required to complete this method */
    Node delete(Node head, int k) {
        // Your code here
        if (k == 1) {
            return null;
        }

        Node start = head;
        Node temp = head;

        while (start != null) {
            for (int i = 1; i < k; i++) {
                temp = start;
                start = start.next;
                if (start == null) {
                    return head;
                }
            }
            temp.next = start.next;
            start = start.next;
        }

        return head;
    }
}
