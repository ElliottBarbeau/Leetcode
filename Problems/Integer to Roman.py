class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1000: 'M',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'LC',
            50: 'L',
            40: 'XL',
            10: 'X',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        
        res = ''
        mynum = num
        
        while mynum > 0:
            print(mynum, res)
            for key in d.keys():
                while mynum >= key:
                    mynum -= key
                    res += d[key]
        
        return res

print(Solution().intToRoman(1487))