"""
LeetCode 217 - Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/

Problem:
    Given an integer array `nums`, return True if any value appears at least
    twice in the array, and False if every element is distinct.

Approach:
    Insert elements into a hash set one by one; if a value is already present
    we have found a duplicate. Equivalent to comparing len(set) with len(list)
    at the end but allows early exit.

Complexity:
    Time:  O(n)
    Space: O(n)

Example:
    Input:  nums = [1, 2, 3, 1]
    Output: True
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))        # True
    print(contains_duplicate([1, 2, 3, 4]))        # False
    print(contains_duplicate([1, 1, 1, 3, 3, 4]))  # True
