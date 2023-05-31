# Created by Moontasir Abtahee at 5/26/2023

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        lcp = ""
        for i in zip(*strs):
            if len(set(i))==1:
                lcp += i[0]
            else:
                break

        return lcp

longestCommonPrefix = Solution()
print(longestCommonPrefix.longestCommonPrefix(["flower","flow","flight"]))