class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if s[i : j + 1] in wordDict:
                        dp[j + 1] = True
        
        return dp[-1]



s = "leetcode"
wordDict = ["leet", "code"]
print(Solution().wordBreak(s, wordDict))

s = "applepenapple"
wordDict = ["apple", "pen"]
print(Solution().wordBreak(s, wordDict))