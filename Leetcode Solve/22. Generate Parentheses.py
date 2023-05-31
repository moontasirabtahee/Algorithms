# # Created by Moontasir Abtahee at 5/26/2023
#
# # Feature: #Enter feature name here
# # Enter feature description here
#
# # Scenario: # Enter scenario name here
# # Enter steps here
#
# """
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# """
# from itertools import permutations
# class Solution:
#     def generateParenthesis(self, n: int) -> list[str]:
#         output = []
#         for i in permutations(["(",")"]*n,n*2):
#             if self.isValid("".join(i)):
#                 output.append("".join(i))
#
#         return set(output)
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for i in s:
#             if i in ["("]:
#                 stack.append(i)
#             else:
#                 if stack == []:
#                     return False
#                 else:
#                     temp = stack.pop()
#                     if temp == "(" and i != ")":
#                         return False
#         if stack == []:
#             return True
#         else:
#             return False
#
#
# generateParenthesis = Solution()
# print(generateParenthesis.generateParenthesis(6))

"""
the problem of avobe code is it takes much tiime to run
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        output = []
        self.backtrack(output,"",0,0,n)
        return output

    def backtrack(self,output,cur_str,open,close,max):
        if len(cur_str) == max*2:
            output.append(cur_str)
            return
        if open < max:
            self.backtrack(output,cur_str+"(",open+1,close,max)
        if close < open:
            self.backtrack(output,cur_str+")",open,close+1,max)


generateParenthesis = Solution()
print(generateParenthesis.generateParenthesis(6))

