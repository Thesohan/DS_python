"""
Problem Description
https://www.interviewbit.com/problems/rain-water-trapped/
Given an integer array A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



Problem Constraints
1 <= |A| <= 100000



Input Format
The only argument given is integer array A.



Output Format
Return the total water it is able to trap after raining.



Example Input
Input 1:

 A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Input 2:

 A = [1, 2]


Example Output
Output 1:

 6
Output 2:

 0


Example Explanation
Explanation 1:


 In this case, 6 units of rain water (blue section) are being trapped.
Explanation 2:

 No water is trapped.
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        left = [0] * n
        right = [0] * n
        max_so_far = 0
        for i in range(n):
            left[i] = max_so_far
            max_so_far = max(max_so_far, A[i])
        max_so_far = 0
        for i in range(n - 1, -1, -1):
            right[i] = max_so_far
            max_so_far = max(max_so_far, A[i])
        ans = 0
        for i in range(n):
            min_val = min(left[i], right[i])
            if min_val - A[i] > 0:
                ans += min_val - A[i]
        return ans

"""
Another solution
One iteration

"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        max_left_so_far, max_right_so_far = 0, 0
        l, h = 0, n - 1
        water = 0
        while l <= h:
            if A[l] < A[h]:
                if A[l] > max_left_so_far:
                    max_left_so_far = A[l]
                else:
                    water += max_left_so_far - A[l]
                l += 1
            else:
                if A[h] > max_right_so_far:
                    max_right_so_far = A[h]
                else:
                    water += max_right_so_far - A[h]
                h -= 1
        return water


