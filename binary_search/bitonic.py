"""
https://www.interviewbit.com/problems/search-in-bitonic-array/
Problem Description

Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.


Problem Constraints
3 <= N <= 105

1 <= A[i], B <= 108

Given array always contain a bitonic point.

Array A always contain distinct elements.



Input Format
First argument is an integer array A denoting the bitonic sequence.

Second argument is an integer B.



Output Format
Return a single integer denoting the position (0 index based) of the element B in the array A if B doesn't exist in A return -1.



Example Input
Input 1:

 A = [3, 9, 10, 20, 17, 5, 1]
 B = 20
Input 2:

 A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
 B = 30


Example Output
Output 1:

 3
Output 2:

 -1


Example Explanation
Explanation 1:

 B = 20 present in A at index 3
Explanation 2:

 B = 30 is not present in A
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def find_bitonic(self, A, low, high):
        while low < high:
            mid = low + (high - low) // 2
            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
                low = mid + 1
            elif A[mid] < A[mid - 1] and A[mid] > A[mid + 1]:
                high = mid
        return low

    def binary_search(self, A, low, high, item, reverse):
        # print(low,high,item)
        while low < high:
            mid = low + (high - low) // 2
            if not reverse:
                if A[mid] == item:
                    return mid
                elif A[mid] > item:
                    low = mid + 1
                else:
                    high = mid

            else:
                if A[mid] == item:
                    return mid
                elif A[mid] > item:
                    high = mid
                else:
                    low = mid + 1
        return -1

    def solve(self, A, B):
        """
         A=[5, 6, 7, 8, 9, 10, 3, 2, 1]
         B=7
        """
        bitonic_point = self.find_bitonic(A, 0, len(A))
        index = self.binary_search(A, 0, bitonic_point + 1, B, True)
        if index == -1:
            index = self.binary_search(A, bitonic_point + 1, len(A), B, False)
        return index



