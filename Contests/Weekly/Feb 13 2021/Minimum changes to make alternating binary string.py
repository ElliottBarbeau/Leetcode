class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0
        count2 = 0
        expected = '0'
        for i in range(len(s)):
            if s[i] != expected:
                count1 += 1
            if expected == '0':
                expected = '1'
            else:
                expected = '0'
                
        expected = '1'
        for i in range(len(s)):
            if s[i] != expected:
                count2 += 1
            if expected == '0':
                expected = '1'
            else:
                expected = '0'
                
        return min(count1, count2)