from collections import deque
class Solution:
    def highestPeak(self, isWater):
        self.seen = set()
        self.ans = [[-1 for i in range(len(isWater[0]))] for j in range(len(isWater))]
        self.queue = deque()
        for row in range(len(isWater)):
            for column in range(len(isWater[0])):
                if isWater[row][column] == 1:
                    self.ans[row][column] = 0
                    self.queue.append(((row, column), 0))

        while self.queue:
            coord = self.queue.popleft()
            self.bfs(isWater, coord[0][0], coord[0][1], coord[1])
            
        return self.ans
            
    def bfs(self, isWater, row, column, height):
        if (row, column) in self.seen:
            return
        self.seen.add((row, column))
        self.ans[row][column] = height
        if row < len(isWater) - 1:
            self.queue.append(((row + 1, column), height + 1))
        if row > 0:
            self.queue.append(((row - 1, column), height + 1))
        if column < len(isWater[0]) - 1:
            self.queue.append(((row, column + 1), height + 1))
        if column > 0:
            self.queue.append(((row, column - 1), height + 1))