"""
LeetCode 141 - Linked List Cycle (Easy)
https://leetcode.com/problems/linked-list-cycle/

Problem:
    Given the head of a linked list, determine whether the list contains a
    cycle (some node's `next` pointer refers back to a previously visited
    node).

Approach:
    Floyd's Tortoise and Hare. Move a slow pointer one step and a fast
    pointer two steps at a time. If the list has a cycle, the two pointers
    must eventually meet inside it. If fast reaches the end, the list is
    cycle-free.

Complexity:
    Time:  O(n)
    Space: O(1)

Example:
    Input:  head = [3, 2, 0, -4], cycle starts at index 1
    Output: True
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    # Build 3 -> 2 -> 0 -> -4 -> (back to 2)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # create cycle
    print(has_cycle(n1))  # True

    # Build 1 -> 2 (no cycle)
    a = ListNode(1, ListNode(2))
    print(has_cycle(a))   # False
