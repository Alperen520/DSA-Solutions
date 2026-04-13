"""
LeetCode 33 - Search in Rotated Sorted Array (Medium)
https://leetcode.com/problems/search-in-rotated-sorted-array/

Problem:
    There is an integer array `nums` sorted in ascending order (with
    distinct values). Prior to being passed to your function, `nums` is
    possibly rotated at some unknown pivot. Given the array after rotation
    and an integer `target`, return the index of `target` if it is in the
    array, else -1. Must run in O(log n).

Approach:
    Modified binary search. At each step, at least one of the two halves
    (low..mid or mid..high) is guaranteed to be sorted. Check which half
    is sorted, then decide if target lies inside that sorted half; if yes,
    recurse into it, otherwise search the other half.

Complexity:
    Time:  O(log n)
    Space: O(1)

Example:
    Input:  nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(search([1], 0))                    # -1
