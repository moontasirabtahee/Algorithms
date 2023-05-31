# Created by Moontasir Abtahee at 5/26/2023

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

#convert roman to integer number
"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
convert them into a dictonary name numbers

then write a for loop which will iterate from to last to first of given string
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = numbers[s[-1]]
        print(total)
        for i in range(len(s)-2,-1,-1):
            if numbers[s[i]] < numbers[s[i+1]]:
                total -= numbers[s[i]]
            else:
                total += numbers[s[i]]
        return total


print(Solution.romanToInt("self","MCMXCIV"))

