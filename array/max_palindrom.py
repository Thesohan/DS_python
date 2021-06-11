"""
link: https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

"""
class Solution:
    def expend_around_center(self, s: str, left: int, right: int, length: int) -> int:
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        start, end = 0, 0
        n = len(s)
        for i in range(0, n):
            len1 = self.expend_around_center(s, i, i, n)
            len2 = self.expend_around_center(s, i, i + 1, n)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        print(start, end)
        return s[start:end + 1]


