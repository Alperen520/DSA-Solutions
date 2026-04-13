"""
LeetCode 100 - Same Tree (Easy)
https://leetcode.com/problems/same-tree/

Problem:
    Given the roots of two binary trees `p` and `q`, return True if the
    trees are structurally identical AND every corresponding pair of nodes
    has the same value.

Approach:
    Recursive DFS. Two empty trees are equal. If exactly one is empty or
    the values differ, they are not equal. Otherwise recurse on both
    subtrees.

Complexity:
    Time:  O(min(n, m)) - we stop as soon as we find a mismatch
    Space: O(min(h_p, h_q)) - recursion depth

Example:
    Input:  p = [1, 2, 3], q = [1, 2, 3]
    Output: True
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == "__main__":
    a = TreeNode(1, TreeNode(2), TreeNode(3))
    b = TreeNode(1, TreeNode(2), TreeNode(3))
    c = TreeNode(1, TreeNode(2), None)
    print(is_same_tree(a, b))  # True
    print(is_same_tree(a, c))  # False
