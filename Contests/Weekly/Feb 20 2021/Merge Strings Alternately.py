class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = 0, 0
        new = ""
        while w1 < len(word1) and w2 < len(word2):
            new += word1[w1]
            new += word2[w1]
            w1 += 1
            w2 += 1
            
        if w1 == len(word1):
            new += word2[w2:]
            
        if w2 == len(word2):
            new += word1[w1:]
            
        return new