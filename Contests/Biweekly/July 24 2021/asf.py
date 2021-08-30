class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        news = ""
        flag = False
        i = 0
        while i < len(num):
            if change[int(num[i])] > int(num[i]) and not flag:
                flag = True
                news += str(change[int(num[i])])
                i += 1
                while i < len(num) and change[int(num[i])] >= int(num[i]):
                    print(num[i])
                    news += str(change[int(num[i])])
                    i += 1
            else:
                news += num[i]
                i += 1
                
        return news

num = "334111"
change = [0,9,2,3,3,2,5,5,5,5]
print(Solution().maximumNumber(num, change))