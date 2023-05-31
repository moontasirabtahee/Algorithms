# Created by Moontasir Abtahee at 5/26/2023

# Feature: #Enter feature name here
# Enter feature description here

# Scenario: # Enter scenario name here
# Enter steps here
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         triplets = []
#         for i in range(len(nums)):
#            for j in range(i,len(nums)):
#                for k in range(j,len(nums)):
#                    if i!=j and i!=k and j!=k:
#                        if nums[i]+nums[j]+nums[k] == 0:
#                            triplets.append([nums[i],nums[j],nums[k]])
#         for i in triplets:
#             i.sort()
#         triplets = set(tuple(i) for i in triplets)
#         return list(triplets)

# threeSum = Solution()
# print(threeSum.threeSum([-1,0,1,2,-1,-4]))

"""
Time Limit Exceeded
"""

"""
Sort the array (in time O(n * log(n))).
Now for each element i, do the following steps
Set two pointers left — j = i + 1 and right — k = nums.length - 1.
Check if nums[i] + nums[j] + nums[k] == 0 and if it is zero, add these three numbers to the resultant list.
If the sum nums[i] + nums[j] + nums[k] < 0, this means we can move left pointer forward because since the array is sorted and the sum is less than zero, therefore, it makes sense to check for greater value to make the sum bigger.
If the sum nums[i] + nums[j] + nums[k] > 0, this means we are too right and can move the right pointer backward because since the array is sorted and the sum is greater than zero, therefore, it makes sense to check for smaller value to make the sum lesser.
In between loops, we also need to make sure that we are not checking for duplicate values.
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[i]+ nums[left]+nums[right]==0:
                    triplets.append([nums[i],nums[left],nums[right]])
                    left+=1

                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif nums[i]+nums[left]+nums[right]<0:
                    left+=1
                else:
                    right-=1

        return triplets



