"""
LeetCode 121 - Best Time to Buy and Sell Stock (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem:
    You are given an array `prices` where prices[i] is the price of a given
    stock on the i-th day. You want to maximize your profit by choosing a
    single day to buy and a different day in the future to sell. Return the
    maximum profit; if no profit is possible, return 0.

Approach:
    Track the minimum price seen so far while scanning left to right. At each
    day, the best profit if we sell today equals price - min_so_far. Keep the
    running maximum of these values.

Complexity:
    Time:  O(n) - single pass
    Space: O(1) - only two scalar variables

Example:
    Input:  prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6).
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = float("inf")
    best = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > best:
            best = price - min_price
    return best


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
    print(max_profit([7, 6, 4, 3, 1]))     # 0
    print(max_profit([2, 4, 1]))           # 2
