# Created by Moontasir Abtahee at 5/26/2023

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

"""
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return s
                if abs(s - target) < abs(result - target):
                    result = s
                if s < target:
                    left += 1
                else:
                    right -= 1

        return result



