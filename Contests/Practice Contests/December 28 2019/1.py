class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        ans = []
        if n % 2 == 0:
            for i in range(1, (n // 2) + 1):
                ans.append(i)
                ans.append(-i)
        else:
            ans.append(0)
            for i in range(1, (n // 2) + 1):
                ans.append(i)
                ans.append(-i)

        return ans
