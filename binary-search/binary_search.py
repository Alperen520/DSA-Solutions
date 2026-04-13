"""
LeetCode 704 - Binary Search (Easy)
https://leetcode.com/problems/binary-search/

Problem:
    Given a sorted (ascending) array of integers `nums` and an integer
    `target`, write a function to search `target` in `nums`. If target
    exists, then return its index. Otherwise, return -1. You must write an
    algorithm with O(log n) runtime complexity.

Approach:
    Classic iterative binary search. Keep `low` and `high` pointers. At
    each step compute `mid = (low + high) // 2` and compare nums[mid] to
    target. Narrow the search range by half until found or exhausted.

Complexity:
    Time:  O(log n)
    Space: O(1)

Example:
    Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))   # 4
    print(search([-1, 0, 3, 5, 9, 12], 2))   # -1
    print(search([5], 5))                    # 0
