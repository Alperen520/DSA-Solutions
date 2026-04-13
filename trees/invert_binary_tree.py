"""
LeetCode 226 - Invert Binary Tree (Easy)
https://leetcode.com/problems/invert-binary-tree/

Problem:
    Given the root of a binary tree, invert it (mirror image) and return its
    root. Every left subtree becomes the right subtree and vice versa.

Approach:
    Recursive DFS. For each node, swap the left and right children and then
    recurse into both subtrees. Base case: null node returns null.

Complexity:
    Time:  O(n) - each node visited once
    Space: O(h) - recursion depth, h = tree height (O(n) worst case)

Example:
    Input:      4                    Output:     4
              /   \\                              /   \\
             2     7                             7     2
            / \\   / \\                           / \\   / \\
           1   3 6   9                         9   6 3   1
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def level_order(root):
    if not root:
        return []
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


if __name__ == "__main__":
    root = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)))
    print(level_order(invert_tree(root)))  # [4, 7, 2, 9, 6, 3, 1]
