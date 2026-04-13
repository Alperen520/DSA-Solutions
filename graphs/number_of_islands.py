"""
LeetCode 200 - Number of Islands (Medium)
https://leetcode.com/problems/number-of-islands/

Problem:
    Given an m x n 2D binary grid `grid` which represents a map of '1's
    (land) and '0's (water), return the number of islands. An island is
    surrounded by water and is formed by connecting adjacent lands
    horizontally or vertically.

Approach:
    Iterate every cell. When we hit a land cell that hasn't been visited,
    increment our island counter and run DFS to mark all connected land
    cells as visited (here, mutate them to '0' in place to save memory).

Complexity:
    Time:  O(m * n) - each cell visited at most twice
    Space: O(m * n) worst case recursion stack for a grid that is all land

Example:
    Input:  grid = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
    Output: 3
"""

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(num_islands(grid))  # 3
