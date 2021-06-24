class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        arr.sort()
        s = 0
        n = len(arr)
        
        for i in range(n):
            ans = round((target - s) / (n - i))
            if ans < arr[i]:
                return ans
            
            s += arr[i]
            
        return arr[i]
                
        