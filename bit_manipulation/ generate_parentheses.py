"""
link: https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        total_parentheses = n * 2
        res = []
        for i in range(2 ** (total_parentheses - 1), 2 ** total_parentheses):
            nested_list = ""
            left_count = 0
            right_count = 0
            num = i
            while num != 0:
                if (num & 1) == 0:
                    left_count += 1
                    nested_list += "("
                elif right_count < left_count:
                    right_count += 1
                    nested_list += ")"
                num = num >> 1
            if left_count == right_count and len(nested_list) == total_parentheses:
                res.append(nested_list)
        return res
