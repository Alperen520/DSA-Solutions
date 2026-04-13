"""
LeetCode 322 - Coin Change (Medium)
https://leetcode.com/problems/coin-change/

Problem:
    You are given an integer array `coins` representing coins of different
    denominations and an integer `amount` representing a total amount of
    money. Return the fewest number of coins needed to make up that amount.
    If that amount cannot be made up, return -1. You have an infinite number
    of each kind of coin.

Approach:
    Bottom-up DP. Let dp[x] be the minimum coins needed to form amount x.
    Initialize dp[0] = 0 and everything else to infinity. For each amount
    x from 1 to target, try every coin c: if c <= x, update
    dp[x] = min(dp[x], dp[x-c] + 1).

Complexity:
    Time:  O(amount * len(coins))
    Space: O(amount)

Example:
    Input:  coins = [1, 2, 5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for x in range(1, amount + 1):
        for c in coins:
            if c <= x and dp[x - c] + 1 < dp[x]:
                dp[x] = dp[x - c] + 1
    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    print(coin_change([1, 2, 5], 11))  # 3
    print(coin_change([2], 3))         # -1
    print(coin_change([1], 0))         # 0
