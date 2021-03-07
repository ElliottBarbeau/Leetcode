class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        closest = float('inf')
        ans = -1
        for i in range(len(points)):
            #abs(x1 - x2) + abs(y1 - y2)
            if abs(points[i][0] - x) + abs(points[i][1] - y) < closest and (points[i][0] == x or points[i][1] == y):
                closest = abs(points[i][0] - x) + abs(points[i][1] - y)
                ans = i
                
        return ans