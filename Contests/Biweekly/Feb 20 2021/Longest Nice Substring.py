class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        d = {}
        nice = []
        ret = ""
        for char in s:
            if char not in d:
                d[char] = 1
            if char.swapcase() in d:
                nice.append(char)
                nice.append(char.swapcase())
                
        if not nice:
            return ""
        
        longest = 0
        for i in range(len(s)):
            unmatched = {}
            matched = {}
            if s[i] in nice:
                unmatched[s[i]] = 1
                for j in range(i + 1, len(s)):
                    if s[j] not in unmatched and s[j] not in matched:
                        if s[j].swapcase() in unmatched:
                            del[unmatched[s[j].swapcase()]]
                            matched[s[j]] = 1
                            matched[s[j].swapcase()] = 1
                        else:
                            unmatched[s[j]] = 1
                        
                    if len(unmatched) == 0:
                        if j - i + 1 > longest:
                            longest = j - i + 1
                            ret = s[i : j + 1]
                            
        return ret