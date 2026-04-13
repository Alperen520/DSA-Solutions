"""
LeetCode 125 - Valid Palindrome (Easy)
https://leetcode.com/problems/valid-palindrome/

Problem:
    A phrase is a palindrome if, after converting all uppercase letters to
    lowercase and removing all non-alphanumeric characters, it reads the
    same forward and backward. Given a string `s`, return True if it is a
    palindrome, or False otherwise.

Approach:
    Two pointers from both ends. Skip non-alphanumeric characters and
    compare lowercase values. This avoids building a cleaned copy of the
    string, keeping memory O(1).

Complexity:
    Time:  O(n)
    Space: O(1)

Example:
    Input:  s = "A man, a plan, a canal: Panama"
    Output: True
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))                       # False
    print(is_palindrome(" "))                                # True
