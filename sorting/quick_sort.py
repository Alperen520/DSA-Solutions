"""
Quick Sort - Divide & Conquer Sorting via Partitioning
Reference: https://en.wikipedia.org/wiki/Quicksort

Problem:
    Sort an array of integers in ascending order using quick sort. In-place,
    comparison-based sort that is usually the fastest general-purpose sort
    in practice thanks to cache-friendly access patterns.

Approach:
    1. Pick a pivot (here, the last element of the current range).
    2. Partition: rearrange so all elements <= pivot come before it and all
       greater come after.
    3. Recursively sort the two partitions.

Complexity:
    Time:  O(n log n) average, O(n^2) worst case (already-sorted + bad pivot)
    Space: O(log n) average recursion depth

Example:
    Input:  [10, 7, 8, 9, 1, 5]
    Output: [1, 5, 7, 8, 9, 10]
"""

from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    arr = arr.copy()  # avoid mutating caller's list
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pivot_index = _partition(arr, low, high)
        _quick_sort(arr, low, pivot_index - 1)
        _quick_sort(arr, pivot_index + 1, high)


def _partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    print(quick_sort([10, 7, 8, 9, 1, 5]))  # [1, 5, 7, 8, 9, 10]
    print(quick_sort([]))                    # []
    print(quick_sort([2, 2, 2]))             # [2, 2, 2]
    print(quick_sort([3, -1, 0, 5, -2]))     # [-2, -1, 0, 3, 5]
