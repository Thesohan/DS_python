"""
https://www.interviewbit.com/problems/square-root-of-integer/
Given an integar A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY



Input Format

The first and only argument given is the integer A.
Output Format

Return floor(sqrt(A))
Constraints

1 <= A <= 10^9
For Example

Input 1:
    A = 11
Output 1:
    3

Input 2:
    A = 9
Output 2:
    3
"""
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A <= 1:
            return A
        low = 0
        high = A
        while low < high:
            mid = low + (high - low) // 2
            sqr = mid * mid
            if sqr == A:
                return mid
            elif sqr < A:
                low = mid + 1
            else:
                high = mid
        return low - 1

