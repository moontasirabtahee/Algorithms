# # Created by Moontasir Abtahee at 5/25/2023
#
# # Feature: #Enter feature name here
# # Enter feature description here
#
# # Scenario: # Enter scenario name here
# # Enter steps here
# """
# read in and ignore whitespace
# check if next char is + or -
# read in next char
# while next char is digit
#     add digit to number
#     read in next char
# return sign * number
#
#
#
# """
#
# class Solution:
#     def myAtoi1(self, s: str) -> int:
#         sign =""
#         number = str()
#         flag = 0
#         for i in s:
#             if i == " ":
#
#                 continue
#             elif i == "+":
#                 if sign == "":
#                     sign = "+"
#                 elif flag == 1:
#                     return 0
#                 else:
#                     return 0
#             elif i == "-":
#                 if sign == "":
#                     sign = "-"
#                 elif flag == 1:
#                     return 0
#                 else:
#                     return 0
#             elif i.isdigit():
#                 flag = 1
#                 number += i
#             else:
#                 break
#         if number == "":
#             return 0
#         else:
#             if sign == "-":
#                 number = -int(number)
#             else:
#                 number = int(number)
#
#         if number>2**31-1:
#             return 2**31-1
#         elif number<-2**31:
#             return -2**31
#         else:
#             return number
#
#
# """
# Wrong Answer
#
# 1071 / 1084 testcases passed
# Input
# s =
# "00000-42a1234"
# Use Testcase
# Output
# -42
# Expected
# 0
# """
#
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         sign = ""
#         number = str()
#         flag = 0
#         for i in range(len(s)):
#             if s[i] == " ":
#                 continue
#             elif s[i] == "+":
#                 if sign == "":
#                     sign = "+"
#                 else:
#                     return 0
#             elif s[i] == "-" and len(number)==0:
#                 if sign == "":
#                     sign = "-"
#                 else:
#                     return 0
#             elif s[i].isdigit():
#                 number += s[i]
#             else:
#                 if len(number)>0:
#                     break
#         if number == "":
#             return 0
#         else:
#             if sign == "-":
#                 number = -int(number)
#             else:
#                 number = int(number)
#
#         if number>2**31-1:
#             return 2**31-1
#         elif number<-2**31:
#             return -2**31
#         else:
#             return number
#
#
# s = Solution()
# print(s.myAtoi("00000-42a1234"))
# print(s.myAtoi("42"))
#
#
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = ""
        number = str()
        s = s.strip()
        if len(s) == 0:
            return 0
        for i in s:
            if i == "+":
                if len(sign)>0:
                    if len(number)>0:
                        break
                    return 0
                sign = "+"

            elif i == "-":
                if len(sign)>0:
                    if len(number)>0:
                        break
                    return 0
                sign = "-"


            elif i.isdigit():
                if len(sign)==0:
                    sign = "+"
                number += i
            else:
                break

        if number == "":
            return 0
        else:
            if sign == "-":
                number = -int(number)
            else:
                number = int(number)

        if number>2**31-1:
            return 2**31-1
        elif number<-2**31:
            return -2**31
        else:
            return number




s = Solution()
print(s.myAtoi("   -42"))