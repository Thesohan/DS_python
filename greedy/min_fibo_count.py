"""
https://www.interviewbit.com/problems/sum-of-fibonacci-numbers/
How many minimum numbers from fibonacci series are required such that sum of numbers should be equal to a given Number N?
Note : repetition of number is allowed.

Example:

N = 4
Fibonacci numbers : 1 1 2 3 5 .... so on
here 2 + 2 = 4
so minimum numbers will be 2
"""
class Solution:
    # @param A : integer
    # @return an integer
    def cal_fibo(self, A):
        while True:
            if A >= self.fib[-1] + self.fib[-2]:
                self.fib.append(self.fib[-1] + self.fib[-2])
            else:
                break

    def fibsum(self, A):
        self.fib = [1, 1]
        self.cal_fibo(A)
        count = 0
        i = -1
        while A:
            while A >= self.fib[i]:
                A -= self.fib[i]
                count += 1
            i -= 1
        return count
