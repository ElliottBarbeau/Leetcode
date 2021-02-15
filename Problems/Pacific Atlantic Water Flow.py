# Come back to this question another time
class Solution:
    def pacificAtlantic(self, grid):
        res = []
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if self.dfs(grid, row, column, grid[row][column]):
                    res.append([row, column])

        return res

    def dfs(self, grid, row, column, prev):
        if row < 0 or column < 0 or row > len(grid) - 1 or column > len(grid[0]) - 1:
            return True
        
        if 0 <= row < len(grid) and 0 <= column < len(grid[0]) and grid[row][column] > prev:
            return False

        up = self.dfs(grid, row + 1, column, grid[row][column])
        down = self.dfs(grid, row - 1, column, grid[row][column])
        left = self.dfs(grid, row, column - 1, grid[row][column])
        right = self.dfs(grid, row, column + 1, grid[row][column])

        return (up or left) and (right or down)

grid = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(Solution().pacificAtlantic(grid))