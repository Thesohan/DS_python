"""
Problem
Given 2 strings, P and T, find the number of occurrences of P in T.

Input:

First line contains string P, and second line contains the string T.

Output:

Print a single integer, the number of occurrences of P in T.

Constraints:


Sample Input
sda
sadasda
Sample Output
1
"""
def find_lps(p, lps, m):
    length = 0
    i = 1
    while i < m:
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length -= 1
            else:
                lps[i] = length
                i += 1
    # print(lps)
    """
  p=aab
  t=aacaabaabcd
  """


def find_pattern(p, t, m, n):
    i = 0
    j = 0
    count = 0
    while i < n:
        if p[j] == t[i]:
            i, j = i + 1, j + 1

        if j == m:
            count += 1
            j = lps[j - 1]
        elif i < n and p[j] != t[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count


p = input()
t = input()
m = len(p)
n = len(t)
lps = [0] * m
find_lps(p, lps, m)
# print(lps)
print(find_pattern(p, t, m, n))
