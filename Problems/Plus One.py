class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1
        if digits[-1] >= 10:
            s = str(digits[-1])
            digits.pop()
            digits.append(s[0])
            digits.append(s[1])
        return digits

print(Solution().plusOne([9]))