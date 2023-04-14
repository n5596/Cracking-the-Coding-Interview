## Chapter 8 of the Interview Questions section

#### 1. Triple Step: https://leetcode.com/problems/n-th-tribonacci-number/

#### 2. Robot in a Grid: https://leetcode.com/problems/unique-paths-ii/

#### 3. Magic Index (duplicates allowed): https://www.codingninjas.com/codestudio/problems/magic-index_1199229?leftPanelTab=0 (**)

#### 4. Power Set: https://leetcode.com/problems/subsets/ (**)

    Take a look at the combinatorics approach: it's not intuitive at all

#### 5. Recursive Multiply: https://www.codingninjas.com/codestudio/problems/recursive-multiply_1172216?leftPanelTab=0 (**)

    Similar: https://leetcode.com/problems/divide-two-integers/
    
#### 6. Towers of Hanoi: https://www.codingninjas.com/codestudio/problems/tower-of-hanoi_981323?leftPanelTab=0 (**)

#### 7. Permutations without Dups: https://leetcode.com/problems/permutations/ (**)

    Approach 1: Recursively finding the permutations for n-1. Inserting nums[idx] at each possible location in all the perms[n-1].
    
    Approach 2: Recursively find the permutations of substrings and prepend nums[i] (need a loop for i). Non-intuitive so take a look at this.

#### 8. Permutations with Duplicates: https://leetcode.com/problems/permutations-ii/ (**)

#### 9. Parens: https://leetcode.com/problems/generate-parentheses/ (**)

#### 10. Paint Fill: https://leetcode.com/problems/flood-fill/

#### 11. Coins

#### 12. Eight Queens: https://leetcode.com/problems/n-queens/ (**)

#### 13. Stack of Boxes

#### 14. Boolean Evaluation: https://www.codingninjas.com/codestudio/problems/problem-name-boolean-evaluation_1214650?leftPanelTab=1 (** Took me hours)

    Use mod = (10**9)+7 instead of mod = pow(10, 9)+7. The former is an int whereas the latter is a float. If you use the latter, the answer will also be a float and might be wrong when compared to the online judge.
