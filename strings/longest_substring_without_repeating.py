"""
LeetCode 3 - Longest Substring Without Repeating Characters (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem:
    Given a string `s`, find the length of the longest substring without
    repeating characters.

Approach:
    Sliding window with a hash map storing the last index of each character.
    Expand the right boundary one step at a time. If the current character
    was seen inside the current window, jump the left boundary to one past
    its previous index. Track the maximum window length as we go.

Complexity:
    Time:  O(n) - each index enters and leaves the window at most once
    Space: O(min(n, k)) - k is the size of the character alphabet

Example:
    Input:  s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with length 3.
"""


def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))     # 1
    print(length_of_longest_substring("pwwkew"))    # 3
    print(length_of_longest_substring(""))          # 0
