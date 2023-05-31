# Created by Moontasir Abtahee at 5/26/2023

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            else:
                if stack == []:
                    return False
                else:
                    temp = stack.pop()
                    if temp == "(" and i != ")":
                        return False
                    elif temp == "{" and i != "}":
                        return False
                    elif temp == "[" and i != "]":
                        return False
        if stack == []:
            return True
        else:
            return False



