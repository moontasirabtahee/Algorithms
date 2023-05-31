# Created by Moontasir Abtahee at 5/26/2023

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if list(set(p)) == ["*"]:
            return True
        if p == s or p == "*":
            return True
        elif p == "" or s == "":
            return False
        elif p[0] == s[0] or p[0] == "?":
            return self.isMatch(s[1:],p[1:])
        elif p[0] == "*":
            return self.isMatch(s[1:],p) or self.isMatch(s,p[1:])
        else:
            return False

s = ""
p = "******"
print(Solution().isMatch(s,p))

"""Time Limit Exceeded!!! 940"""