"""
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer
"""

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        """
           0,1,2,3,4,5
        A=[1,4,5,3,0,2]

        A=[4,0,2,3,1,5]

        Ex.
        a=10
        b=8
        n=11
        10*11+8=118
        118%11=8
        118/10=11

        """
        n = len(A)

        for i, num in enumerate(A):
            A[i] = (A[num] % n * n) + num
        for i in range(n):
            A[i] = A[i] / n

        return
