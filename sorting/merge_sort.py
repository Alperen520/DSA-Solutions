"""
Merge Sort - Classic Divide & Conquer Sorting Algorithm
Reference: https://en.wikipedia.org/wiki/Merge_sort

Problem:
    Sort an array of integers in ascending order using merge sort. This is a
    stable, comparison-based sort that guarantees O(n log n) time regardless
    of input distribution, making it popular for external sorting and linked
    lists.

Approach:
    1. Recursively split the array into halves until subarrays of length 1.
    2. Merge two sorted halves by walking two pointers and always picking
       the smaller front element.
    3. The recursion tree has log(n) depth, and each level does O(n) merging.

Complexity:
    Time:  O(n log n) - best, average, and worst case
    Space: O(n) - temporary arrays during the merge step

Example:
    Input:  [5, 2, 4, 6, 1, 3]
    Output: [1, 2, 3, 4, 5, 6]
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    print(merge_sort([5, 2, 4, 6, 1, 3]))      # [1, 2, 3, 4, 5, 6]
    print(merge_sort([]))                       # []
    print(merge_sort([1]))                      # [1]
    print(merge_sort([3, 3, 2, 1, 2]))         # [1, 2, 2, 3, 3]
