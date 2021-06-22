class Solution:
    def maximum69Number (self, num: int) -> int:
        news = ""
        flag = False
        num = str(num)
        for i in range(len(num)):
            if num[i] == '9' or flag:
                news += num[i]
            else:
                news += '9'
                flag = True
                
        return int(news)