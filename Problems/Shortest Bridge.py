class Solution:
    def shortestBridge(self, grid) -> int:
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                