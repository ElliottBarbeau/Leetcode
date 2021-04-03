class Solution:
    def letterCasePermutation(self, S: str) -> list[str]:
        l = [S]
        for i in range(len(S)):
            for j in range(len(l)):
                word = l[j]
                if S[i].isalpha():
                    word = word[:i] + word[i].swapcase() + word[i + 1:]
                    l.append(word)
        
        return l

print(Solution().letterCasePermutation("a1b2"))