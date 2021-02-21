class Solution:
    def minOperations(self, boxes: str):
        res = []
        left_ones, right_ones, first = 0, 0, 0
        for i in range(len(boxes)):
            if boxes[i] == '1':
                right_ones += 1
                first += (i * 1)

        res.append(first)
        left = False

        if boxes[0] == '1':
            right_ones -= 1
            left_ones += 1
            
        for i in range(1, len(boxes)):
            if left:
                left_ones += 1
                left = False
            
            print(right_ones, left_ones)
            res.append(res[i-1] - right_ones + left_ones)

            if boxes[i] == '1':
                right_ones -= 1
                left = True
            
        return res

print(Solution().minOperations("110100"))