class Solution:
    def closedIsland(self, grid) -> int:
        count = 0
        for row in range(1, len(grid) - 1):
            for column in range(1, len(grid[0]) - 1):
                if not grid[row][column] and self.dfs(grid, row, column):
                    count += 1

        return count

    def dfs(self, grid, row, column):
        if grid[row][column]:
            return True

        if row <= 0 or column <= 0 or row >= len(grid) - 1 or column >= len(grid[0]) - 1:
            return False

        grid[row][column] = 1

        up = self.dfs(grid, row + 1, column)
        down = self.dfs(grid, row - 1, column)
        left = self.dfs(grid, row, column - 1)
        right = self.dfs(grid, row, column + 1)

        return up and down and left and right