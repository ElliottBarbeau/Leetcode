class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = num[::-1]
        ans = ""
        flag = False
        for i in range(len(num)):
            if int(num[i]) % 2 != 0 or flag:
                ans += num[i]
                flag = True
                
        return ans[::-1]