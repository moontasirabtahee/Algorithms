# Created by Moontasir Abtahee at 5/26/2023

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
"""

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

"""

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not words or not s:
            return []
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        output = []
        for i in range(len(s)-total_len+1):
            temp = s[i:i+total_len]
            temp_list = []
            for j in range(0,total_len,word_len):
                temp_list.append(temp[j:j+word_len])
            temp_list.sort()
            words.sort()
            if temp_list == words:
                output.append(i)
        return output
