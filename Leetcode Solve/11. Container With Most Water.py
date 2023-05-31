# Created by Moontasir Abtahee at 5/26/2023

# Feature: #Enter feature name here
# Enter feature description here

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        maxArea = 0
        while left<right:
            area = min(height[left],height[right])*(right-left)
            maxArea = max(maxArea,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return maxArea
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))