"""
LeetCode 242 - Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/

Problem:
    Given two strings `s` and `t`, return True if `t` is an anagram of `s`,
    and False otherwise. An anagram uses exactly the same letters with the
    same frequencies, just in a possibly different order.

Approach:
    Count letter frequencies in both strings and compare the counters.
    If lengths differ the answer is immediately False. Using `collections
    .Counter` is idiomatic; a manual dict or length-26 array works too.

Complexity:
    Time:  O(n) - single pass over each string
    Space: O(1) - at most 26 distinct lowercase letters (or O(k) for k unique chars)

Example:
    Input:  s = "anagram", t = "nagaram"
    Output: True
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False
    print(is_anagram("a", "ab"))             # False
