"""
LeetCode 21 - Merge Two Sorted Lists (Easy)
https://leetcode.com/problems/merge-two-sorted-lists/

Problem:
    Merge two sorted linked lists `list1` and `list2` into one sorted list by
    splicing together their nodes. Return the head of the merged list.

Approach:
    Use a dummy head node to simplify edge cases. Walk both lists with two
    pointers and append the smaller node to the tail. When one list is
    exhausted, attach the remainder of the other.

Complexity:
    Time:  O(n + m)
    Space: O(1) - reuses existing nodes, no new allocation besides dummy

Example:
    Input:  list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy.next


def from_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    a = from_list([1, 2, 4])
    b = from_list([1, 3, 4])
    print(to_list(merge_two_lists(a, b)))  # [1, 1, 2, 3, 4, 4]
