// https://www.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1

// POTD 30.04.2024

// Add two numbers represented by linked lists

// Given two decimal numbers, num1 and num2, represented by linked lists of size n and m respectively. The task is to return a linked list that represents the sum of these two numbers.

// For example, the number 190 will be represented by the linked list, 1->9->0->null, similarly 25 by 2->5->null. Sum of these two numbers is 190 + 25 = 215, which will be represented by 2->1->5->null. You are required to return the head of the linked list 2->1->5->null.

// Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

// Example 1:
// Input:
// n = 2
// num1 = 45 (4->5->null)
// m = 3
// num2 = 345 (3->4->5->null)
// Output:
// 3->9->0->null
// Explanation:
// For the given two linked list (4 5) and (3 4 5), after adding the two linked list resultant linked list will be (3 9 0).

// Example 2:
// Input:
// n = 4
// num1 = 0063 (0->0->6->3->null)
// m = 2
// num2 = 07 (0->7->null)
// Output:
// 7->0->null
// Explanation:
// For the given two linked list (0 0 6 3) and (0 7), after adding the two linked list resultant linked list will be (7 0).
// Your Task:
// The task is to complete the function addTwoLists() which has node reference of both the linked lists and returns the head of the sum list.

// Expected Time Complexity: O(n+m)
// Expected Auxiliary Space: O(max(n,m)) for the resultant list.

import java.util.*;

class Node {
    int data;
    Node next;

    Node(int d) {
        data = d;
        next = null;
    }
}

public class AddTwoNumbersRepresentedbyLinkedLists {

    static void printList(Node n) {
        while (n != null) {
            System.out.print(n.data + " ");
            n = n.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int val = sc.nextInt();

        Node num1 = new Node(val);
        Node tail = num1;
        for (int i = 0; i < n - 1; i++) {
            val = sc.nextInt();
            tail.next = new Node(val);
            tail = tail.next;
        }

        int m = sc.nextInt();
        val = sc.nextInt();

        Node num2 = new Node(val);
        tail = num2;
        for (int i = 0; i < m - 1; i++) {
            val = sc.nextInt();
            tail.next = new Node(val);
            tail = tail.next;
        }

        Node res = Solution.addTwoLists(num1, num2);
        printList(res);

        sc.close();
    }
}

class Solution {
    static Node reverseList(Node head) {
        Node p = head, pre = null;

        while (p != null) {
            Node nxt = p.next;
            p.next = pre;
            pre = p;
            p = nxt;
        }

        return pre;
    }

    static Node addTwoLists(Node num1, Node num2) {
        if (num1 == null)
            return num2;

        if (num2 == null)
            return num1;

        num1 = reverseList(num1);
        num2 = reverseList(num2);

        Node dummy = new Node(-1);
        Node p = dummy;

        int carry = 0;
        while (num1 != null || num2 != null || carry == 1) {
            int sum = 0;
            if (num1 != null) {
                sum += num1.data;
                num1 = num1.next;
            }

            if (num2 != null) {
                sum += num2.data;
                num2 = num2.next;
            }

            if (carry == 1)
                sum += carry;

            int val = sum % 10;
            carry = sum / 10;

            p.next = new Node(val);
            p = p.next;
        }

        dummy.next = reverseList(dummy.next);
        p = dummy.next;

        while (p != null && p.data == 0)
            p = p.next;

        return p == null ? new Node(0) : p;
    }
}