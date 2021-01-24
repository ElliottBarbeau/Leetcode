class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        #acac, bd
        def condition_1(a, b):
            
        
        def condition_2(a, b):
            
            
        
        def condition_3(a, b):
            d = {}
            for char in a:
                if char not in d:
                    d[char] = 0
                d[char] += 1
                
            for char in b:
                if char not in d:
                    d[char] = 0
                d[char] += 1
                
            total_len = len(a) + len(b)

            return total_len - max(d.values())
            
        return min(condition_1(a, b), condition_2(a, b), condition_3(a, b))

print(Solution().minCharacters('ace', 'abe'))