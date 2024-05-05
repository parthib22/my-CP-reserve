// https://www.geeksforgeeks.org/problems/k-distance-from-root/1

// POTD 03.05.2024

// K distance from root

// Given a binary tree having n nodes and an integer k. Print all nodes that are at distance k from the root (root is considered at distance 0 from itself). Nodes should be printed from left to right.

// Example 1:
// Input:
// k = 0
//       1
//     /   \
//    3     2
// Output: 
// 1
// Explanation: 
// 1 is the only node which is 0 distance from the root 1.

// Example 2:
// Input:
// k = 3
//         1
//        /
//       2
//        \
//         1
//       /  \
//      5    3
// Output: 
// 5 3
// Explanation:  
// 5 and 3 are the nodes which are at distance 3 from the root 3.
// Here, returning 3 5 will be incorrect.
// Your Task:
// You don't have to take input. Complete the function Kdistance() that accepts root node and k as parameters and returns the value of the nodes that are at a distance k from the root.

// Expected Time Complexity: O(n).
// Expected Auxiliary Space: O(Height of the Tree).

import java.util.LinkedList;
import java.util.Queue;
import java.io.*;
import java.util.*;

class Node {
    int data;
    Node left;
    Node right;

    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

public class KDistancefromRoot {

    static Node buildTree(String str) {

        if (str.length() == 0 || str.charAt(0) == 'N') {
            return null;
        }

        String ip[] = str.split(" ");
        // Create the root of the tree
        Node root = new Node(Integer.parseInt(ip[0]));
        // Push the root to the queue

        Queue<Node> queue = new LinkedList<>();

        queue.add(root);
        // Starting from the second element

        int i = 1;
        while (queue.size() > 0 && i < ip.length) {

            // Get and remove the front of the queue
            Node currNode = queue.peek();
            queue.remove();

            // Get the current node's value from the string
            String currVal = ip[i];

            // If the left child is not null
            if (!currVal.equals("N")) {

                // Create the left child for the current node
                currNode.left = new Node(Integer.parseInt(currVal));
                // Push it to the queue
                queue.add(currNode.left);
            }

            // For the right child
            i++;
            if (i >= ip.length)
                break;

            currVal = ip[i];

            // If the right child is not null
            if (!currVal.equals("N")) {

                // Create the right child for the current node
                currNode.right = new Node(Integer.parseInt(currVal));

                // Push it to the queue
                queue.add(currNode.right);
            }
            i++;
        }

        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String X[] = br.readLine().trim().split(" ");
        int k = Integer.parseInt(X[0]);
        String s = br.readLine();
        Node root = buildTree(s);
        Tree g = new Tree();
        ArrayList<Integer> nodes = g.Kdistance(root, k);
        for (int i = 0; i < nodes.size(); i++) {
            System.out.print(nodes.get(i) + " ");
        }
    }
}

class Tree {
    // Recursive function to print right view of a binary tree.
    ArrayList<Integer> Kdistance(Node root, int k) {
        // Your code here
        Queue<Node> q = new LinkedList<>();
        Queue<Integer> d = new LinkedList<>();
        ArrayList<Integer> ans = new ArrayList<>();

        q.add(root);
        d.add(0);

        while (q.size() > 0) {
            Node node = q.remove();
            int dist = d.remove();

            if (dist == k) {
                ans.add(node.data);
            }

            if (node.left != null) {
                q.add(node.left);
                d.add(dist + 1);
            }

            if (node.right != null) {
                q.add(node.right);
                d.add(dist + 1);
            }
        }

        return ans;
    }
}