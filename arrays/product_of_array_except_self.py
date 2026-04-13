"""
LeetCode 238 - Product of Array Except Self (Medium)
https://leetcode.com/problems/product-of-array-except-self/

Problem:
    Given an integer array `nums`, return an array `answer` such that
    answer[i] is equal to the product of all the elements of nums except
    nums[i]. Solve it without using division and in O(n) time.

Approach:
    Do two passes. In the first pass, fill answer[i] with the product of all
    elements to the LEFT of i. In the second pass, multiply each answer[i]
    by a running product of elements to the RIGHT of i. The output array
    itself holds the left products, so we only need O(1) extra memory.

Complexity:
    Time:  O(n) - two linear passes
    Space: O(1) - not counting the output array

Example:
    Input:  nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]

    return answer


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))      # [24, 12, 8, 6]
    print(product_except_self([-1, 1, 0, -3, 3])) # [0, 0, 9, 0, 0]
