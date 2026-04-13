"""
LeetCode 1 - Two Sum (Easy)
https://leetcode.com/problems/two-sum/

Problem:
    Given an array of integers `nums` and an integer `target`, return indices
    of the two numbers such that they add up to target. You may assume that
    each input would have exactly one solution, and you may not use the same
    element twice.

Approach:
    Use a hash map to store each number's index as we iterate. For every
    number `n`, check if `target - n` has already been seen. If yes, we have
    found the pair. This turns a naive O(n^2) brute force into a single pass.

Complexity:
    Time:  O(n) - single pass through the array
    Space: O(n) - hash map may store up to n entries

Example:
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] == 9
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))        # [1, 2]
    print(two_sum([3, 3], 6))           # [0, 1]
