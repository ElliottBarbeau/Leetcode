class Solution:
    def freqAlphabets(self, s: str) -> str:
        news = []
        i = 0
        while i < len(s) - 3:
            if s[i] == "#":
                i += 1
                continue

            if s[i + 2] == "#":
                news.append(chr(96 + int(s[i] + s[i + 1])))
                i += 3
            else:
                news.append(chr(96 + int(s[i])))
                i += 1

        if s[-1] == "#":
            news.append(chr(96 + int(s[-3 : -1])))

        else:
            while i < len(s):
                news.append(chr(96 + int(s[-(len(s) - i)])))
                i += 1
        
        return "".join(news)