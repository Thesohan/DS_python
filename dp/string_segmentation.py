"""
Link: https://leetcode.com/problems/word-break/
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
class Solution:
    def __init__(self):
        self.cache={}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        is_visited=self.cache.get(s)
        if is_visited is not None:
            return is_visited
        if s=="":
            self.cache[s]=True
            return True
        result=any([s[:index] in wordDict and self.wordBreak(s[index:],wordDict) for index in range(1,len(s)+1)])
        self.cache[s]=result
        return result