# Created by Moontasir Abtahee at 5/25/2023

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here

# nums = []
# 0 - red , 1 - white , 2 - blue
#inplace dont return anything
# Example 1:
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def sortColor(nums):
    #bubble sort
    for i in range(len(nums)):
        flag = 0
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                flag = 1
        if flag == 0:
            break
