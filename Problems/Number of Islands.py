class Solution:
    def numIslands(self, grid) -> int:
        count = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    self.dfs(grid, row, column)
                    count += 1
                    
        return count
        
    def dfs(self, grid, row, column):
        if 0 <= row < len(grid) and 0 <= column < len(grid[0]) and grid[row][column] == '1':
            grid[row][column] = '0'
            self.dfs(grid, row + 1, column)
            self.dfs(grid, row - 1, column)
            self.dfs(grid, row, column + 1)
            self.dfs(grid, row, column - 1)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))