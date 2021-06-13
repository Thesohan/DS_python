"""
link: https://leetcode.com/problems/subsets/
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        """
        [1,2,3]
        1->3
        10-> 2
        11-> 23
        100-> 1
        101-> 13
        110-> 12
        111-> 123
        """
        res = [[]]
        for i in range(1, 2 ** n):
            nested_list = []
            num = i
            index = n - 1
            while num != 0:
                if (num & 1) != 0:
                    nested_list.append(nums[index])
                index -= 1
                num = num >> 1

            res.append(nested_list)

        return res

