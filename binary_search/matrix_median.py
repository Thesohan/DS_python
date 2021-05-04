"""Given a matrix of integers A of size N x M in which each row is sorted.
https://www.interviewbit.com/problems/matrix-median/
Find an return the overall median of the matrix A.

Note: No extra memory is allowed.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Input Format

The first and only argument given is the integer matrix A.
Output Format

Return the overall median of the matrix A.
Constraints

1 <= N, M <= 10^5
1 <= N*M  <= 10^6
1 <= A[i] <= 10^9
N*M is odd
For Example

Input 1:
    A = [   [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]   ]
Output 1:
    5
Explanation 1:
    A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
    Median is 5. So, we return 5.

Input 2:
    A = [   [5, 17, 100]    ]
Output 2:
    17 ``` Matrix="""

from bisect import bisect_right


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def find_min_max(self, A, r, c):
        minimum = A[0][0]
        maximum = A[0][c - 1]
        for i in range(r):
            minimum = min(minimum, A[i][0])
            maximum = max(maximum, A[i][-1])
        return minimum, maximum

    def find_no_of_small(self, A, end, item):
        beg = 0
        while beg <= end:
            mid = beg + (end - beg) // 2
            if A[mid] == item:
                return mid
            if A[mid] < item:
                beg = mid + 1
            else:
                end = mid - 1
        return 0

    def binSearch(self, matrix, min_el, max_el, cntElBeforeMed):
        start = min_el
        end = max_el
        while start < end:
            mid = start + ((end - start) // 2)
            cnt = 0
            for row in matrix:
                cnt += bisect_right(row, mid)
            if cnt > cntElBeforeMed:
                end = mid
            else:
                start = mid + 1

        return start

    def findMedian(self, A):
        r = len(A)
        c = len(A[0])
        minimum, maximum = self.find_min_max(A, r, c)
        small_count = (r * c) // 2
        return self.binSearch(A, minimum, maximum, small_count)