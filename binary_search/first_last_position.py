"""
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        min_index=-1
        max_index=-1
        first_index=-1
        beg,end=0,len(nums)-1
        while beg<=end:
            mid = beg+(end-beg)//2
            if nums[mid]==target:
                min_index=mid
                end=mid-1
                if min_index==-1:
                    first_index=mid
            elif nums[mid]>target:
                end=mid-1
            else:
                beg=mid+1
        if min_index!=-1:
            beg=first_index
            end=len(nums)-1
            max_index=min_index
            while beg<=end:
                mid = beg+(end-beg)//2
                if nums[mid]==target:
                    max_index=mid
                    beg=mid+1
                elif nums[mid]>target:
                    end=mid-1
                else:
                    beg=mid+1

        return [min_index,max_index]