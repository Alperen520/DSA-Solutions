"""
LeetCode 70 - Climbing Stairs (Easy)
https://leetcode.com/problems/climbing-stairs/

Problem:
    You are climbing a staircase with `n` steps. Each time you can either
    climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Approach:
    Classic Fibonacci recurrence: ways(n) = ways(n-1) + ways(n-2). The
    number of ways to reach step n equals the ways from step (n-1) plus the
    ways from step (n-2). Iteratively track just the last two values to use
    constant space.

Complexity:
    Time:  O(n)
    Space: O(1)

Example:
    Input:  n = 3
    Output: 3
    Explanation: 1+1+1, 1+2, 2+1
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1


if __name__ == "__main__":
    print(climb_stairs(2))  # 2
    print(climb_stairs(3))  # 3
    print(climb_stairs(5))  # 8
