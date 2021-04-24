"""
Problem Description

Reverse the bits of an 32 bit unsigned integer A.

Problem Constraints
0 <= A <= 232

Input Format
First and only argument of input contains an integer A.

Output Format
Return a single unsigned integer denoting the decimal value of reversed bits.

Example Input
Input 1:

 0
Input 2:

 3


Example Output
Output 1:

 0
Output 2:

 3221225472


Example Explanation
Explanation 1:

        00000000000000000000000000000000

=>      00000000000000000000000000000000
Explanation 2:

        00000000000000000000000000000011
=>      11000000000000000000000000000000
"""

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def to_binary(self, A):
        binary = ""
        while A:
            binary = str(A % 2) + binary
            A = A // 2
        return binary

    def to_decimal(self, A):
        decimal = 0
        for i in range(32):
            decimal += 2 ** i if A[31 - i] == '1' else 0
        return decimal

    def reverse(self, A):
        binary_a = self.to_binary(A)
        binary_reverse = binary_a[::-1] + '0' * (32 - len(binary_a))
        return self.to_decimal(binary_reverse)


"""
Another Solution
"""


class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer

    def reverse(self, A):
        return int('{:032b}'.format(A)[::-1], 2)

"""
Another solution
"""


class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer

    def reverse(self, A):
        ans = 0
        for i in range(32):
            if A & (1 << i):
                ans |= (1 << (31 - i))
        return ans
