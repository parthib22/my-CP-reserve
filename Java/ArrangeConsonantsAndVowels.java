// https://www.geeksforgeeks.org/problems/arrange-consonants-and-vowels/1

// POTD 01.05.2024

// Arrange Consonants and Vowels

// Given a singly linked list having n nodes containing english alphabets ('a'-'z'). Rearrange the linked list in such a way that all the vowels come before the consonants while maintaining the order of their arrival. 

// Example 1:
// Input:
// n = 9
// linked list: a -> b -> c -> d -> e -> f -> g -> h -> i 
// Output: 
// a -> e -> i -> b -> c -> d -> f -> g -> h
// Explanation: 
// After rearranging the input linked list according to the condition the resultant linked list will be as shown in output.

// Example 2:
// Input:
// n = 8
// linked list: a -> b -> a -> b -> d -> e -> e -> d 
// Output: 
// a -> a -> e -> e -> b -> b -> d -> d
// Explanation: 
// After rearranging the input linked list according to the condition the resultant linked list will be as shown in output.
// Your Task:
// Your task is to complete the function arrangeCV(), which takes head of linked list and arranges the list in such a way that all the vowels come before the consonants while maintaining the order of their arrival and returns the head of the updated linked list.

// Expected Time Complexity :  O(n)
// Expected Auxiliary Space :  O(1)

// import java.io.*;
import java.util.*;

class Node {
    char data;
    Node next;

    public Node(char data) {
        this.data = data;
        next = null;
    }
}

public class ArrangeConsonantsAndVowels {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Node head = null, tail = null;

        char head_c = sc.next().charAt(0);
        head = new Node(head_c);
        tail = head;

        while (n-- > 1) {
            tail.next = new Node(sc.next().charAt(0));
            tail = tail.next;
        }

        Solution obj = new Solution();
        // show(head);
        show(obj.arrangeCV(head));

        sc.close();
    }

    public static void po(Object o) {
        System.out.println(o);
    }

    public static void show(Node head) {
        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }
        System.out.println();
    }
}

class Solution {

    public Node arrangeCV(Node head) {
        // write code here and return the head of changed linked list

        Node start = head;

        ArrayList<Character> vowelList = new ArrayList<>();
        ArrayList<Character> consonantList = new ArrayList<>();

        char ch;

        while (start != null) {
            ch = start.data;
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                vowelList.add(ch);
            } else {
                consonantList.add(ch);
            }
            start = start.next;
        }

        start = head;
        for (char curr : vowelList) {
            start.data = curr;
            start = start.next;
        }
        for (char curr : consonantList) {
            start.data = curr;
            start = start.next;
        }

        return head;
    }
}