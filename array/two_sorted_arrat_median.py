"""
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        is_odd = False if total % 2 == 0 else True
        m, n = len(nums1), len(nums2)
        if n < m:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        l, r = 0, m - 1
        while True:
            mid = l + (r - l) // 2  # for A
            b_mid = half - mid - 2  # For B
            a_left = nums1[mid] if mid >= 0 else float("-infinity")
            print(mid + 1, m)
            a_right = nums1[mid + 1] if mid + 1 < m else float("infinity")
            b_left = nums2[b_mid] if b_mid >= 0 else float("-infinity")
            b_right = nums2[b_mid + 1] if b_mid + 1 < n else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                # found the ans
                if is_odd:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2

            elif a_left > b_right:
                # shift the
                r = mid - 1
            else:
                l = mid + 1


