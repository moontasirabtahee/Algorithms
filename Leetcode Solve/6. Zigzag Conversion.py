# Created by Moontasir Abtahee at 5/25/2023

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows>=len(s):
            return s
        row = 0
        step = 1
        ans = [""]*numRows
        for i in s:
            ans[row] += i
            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1
            row += step
        return "".join(ans)
