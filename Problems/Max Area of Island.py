class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        max_area = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    max_area = max(max_area, self.dfs(grid, row, column))

        return max_area

    def dfs(self, grid, row, column):
        if 0 <= row < len(grid) and 0 <= column < len(grid[0]) and grid[row][column] == 1:
            grid[row][column] = 0
            return 1 + self.dfs(grid, row + 1, column) + self.dfs(grid, row - 1, column) + self.dfs(grid, row, column + 1) + self.dfs(grid, row, column - 1)
        else:
            return 0

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(Solution().maxAreaOfIsland(grid))