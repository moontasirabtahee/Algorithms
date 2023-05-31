# Created by Moontasir Abtahee at 5/26/2023

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

"""
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        output = []
        if digits == " ":
            return []
        for i in digits:
            if i.isdigit():
                if output == []:
                    output = list(mapping[int(i)])
                else:
                    temp = []
                    for j in output:
                        for k in mapping[int(i)]:
                            temp.append(j+k)
                    output = temp
            else:
                return []

        return output


letterCombinations = Solution()
print(letterCombinations.letterCombinations("23"))