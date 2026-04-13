"""
LeetCode 198 - House Robber (Medium)
https://leetcode.com/problems/house-robber/

Problem:
    You are a robber planning to rob houses along a street. Each house has
    some money stashed; the only constraint is that adjacent houses have
    alarms that connect to each other, so you cannot rob two adjacent
    houses. Given an integer array `nums` representing the amount of money
    at each house, return the maximum amount you can rob tonight.

Approach:
    DP recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i]). At each house,
    decide whether to skip (take dp[i-1]) or rob it (nums[i] plus dp[i-2]).
    Rolling variables keep memory constant.

Complexity:
    Time:  O(n)
    Space: O(1)

Example:
    Input:  nums = [2, 7, 9, 3, 1]
    Output: 12
    Explanation: Rob houses 0, 2, 4 -> 2 + 9 + 1 = 12.
"""

from typing import List


def rob(nums: List[int]) -> int:
    prev2, prev1 = 0, 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)
    return prev1


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))     # 4
    print(rob([2, 7, 9, 3, 1]))  # 12
    print(rob([]))               # 0
