"""
Link:https://leetcode.com/problems/search-in-rotated-sorted-array/
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
"""

class Solution:
    def binary_search(self,nums,beg,end,target):
        while beg<=end:
            mid=beg+(end-beg)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                beg=mid+1
        return -1

    def get_pivot(self,nums,beg,end):
        print(beg,end)
        while beg<=end:
            mid=beg+(end-beg)//2
            if mid<end and nums[mid]>nums[mid+1]:
                return mid
            if beg<mid and nums[mid]<nums[mid-1]:
                return mid-1
            if nums[beg]<nums[mid]:
                beg=mid+1
            else:
                end=mid-1
        return len(nums)-1

    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        beg,end=0,n-1
        pivot=self.get_pivot(nums,0,n-1)
        print(pivot)
        ans=self.binary_search(nums,beg,pivot,target)
        if ans==-1:
            ans=self.binary_search(nums,pivot+1,end,target)
        return ans