Chapter 4 in the Interview Questions section.

1. Route Between Nodes

      Similar (bidirectional graph instead of directed): https://leetcode.com/problems/find-if-path-exists-in-graph/
      
2. Minimal Tree: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/ (**)

3. List of Depths: https://leetcode.com/problems/binary-tree-level-order-traversal/

4. Check Balanced: https://leetcode.com/problems/balanced-binary-tree/ (**)

5. Validate BST: https://leetcode.com/problems/validate-binary-search-tree/ (**)
      
      min-max approach: easier to implement but it's a bit confusing. learn this for interviews.
      
      inorder approach: if we're not using a list to store the nodes in order, it's difficult to implement but the logic is simple

6. Successor: https://www.lintcode.com/problem/448/ (**)

7. Build Order: https://leetcode.com/problems/course-schedule-ii/ (**)

      non-DFS: checking for all nodes with incoming[node] == 0 and adding them to a queue.
      
      DFS: finding nodes on which no other node depends via dfs and adding them to an array in that particular array.

8. First Common Ancestor: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

      via parents: storing parent info and iterating via parents of p and q
      
      optimized DFS: passing flags to declare how many nodes have been found

9. BST Sequences:

10. Check Subtree:

11. Paths with Sum:
