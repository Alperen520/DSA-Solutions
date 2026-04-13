"""
LeetCode 104 - Maximum Depth of Binary Tree (Easy)
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Problem:
    Given the root of a binary tree, return its maximum depth. The maximum
    depth is the number of nodes along the longest path from the root down
    to the farthest leaf node.

Approach:
    Simple DFS. An empty subtree has depth 0. Otherwise depth is
    1 + max(depth(left), depth(right)).

Complexity:
    Time:  O(n)
    Space: O(h) - recursion stack, h = tree height

Example:
    Input:  root = [3, 9, 20, null, null, 15, 7]
    Output: 3
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(max_depth(root))          # 3
    print(max_depth(None))          # 0
    print(max_depth(TreeNode(1)))   # 1
