"""
LeetCode 206 - Reverse Linked List (Easy)
https://leetcode.com/problems/reverse-linked-list/

Problem:
    Given the head of a singly linked list, reverse the list and return the
    new head.

Approach:
    Iterate with three pointers: `prev`, `curr`, and a temporary `next_node`.
    On each step, flip the current node's `next` pointer to the previous
    node, then advance prev and curr. When curr becomes None, prev is the
    new head.

Complexity:
    Time:  O(n)
    Space: O(1)

Example:
    Input:  head = 1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def to_list(head: Optional[ListNode]) -> list:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    # Build 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(to_list(reverse_list(head)))  # [5, 4, 3, 2, 1]
