# Created by Moontasir Abtahee at 5/26/2023

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses
substring

Loop through the string from left to right and store the counts of both type of parentheses in two variables left and right.
If left == right, it means we have valid substring.
We can then find if the length of current valid substring (left + right) is the maximum or not.
If right > left, it means we have invalid string, and we will reset left and right to zero.
Repeat the steps 1-4 looping string from right to left and reset the counters as soon as left > right.
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_len = 0
        for i in s:
            if i == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len,2*right)
            elif right > left:
                left = right = 0

        left = right = 0
        for i in s[::-1]:
            if i == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len,2*left)
            elif left > right:
                left = right = 0

        return max_len

