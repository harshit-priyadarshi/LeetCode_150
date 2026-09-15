"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative order of the remaining characters. 
For example, "ace" is a subsequence of "abcde" while "aec" is not.

Example 1: s = "ace", t = "abcde"
Output: true

Example 2: s = "aec", t = "abcde"
Output: false

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = 0
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
            right += 1

        return left == len(s) 