class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        seen1, seen2 = set(), set()
        islands1, islands2 = [], []
        count = 0
        index = 2
        for row in range(len(grid1)):
            for column in range(len(grid1[row])):
                curr = set()
                self.findIslands(grid1, islands1, row, column, curr, index)
                if curr:
                    islands1.append(curr)
                    index += 1
                
        for row in range(len(grid2)):
            for column in range(len(grid2[row])):
                curr = set()
                self.findIslands(grid2, islands2, row, column, curr, 2)
                if curr:
                    islands2.append(curr)
                   
        for i2 in islands2:
            p0, p1 = i2.pop()
            i2.add((p0, p1))
            val = grid1[p0][p1]
            if val > 0 and i2.issubset(islands1[val - 2]):
                count += 1
                 
        return count
        
    def findIslands(self, grid, islands, row, column, curr, index):
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or grid[row][column] == 0 or grid[row][column] > 1:
            return
        
        if grid[row][column] == 1:
            curr.add((row, column))
            grid[row][column] = index
            
        self.findIslands(grid, islands, row + 1, column, curr, index)
        self.findIslands(grid, islands, row - 1, column, curr, index)
        self.findIslands(grid, islands, row, column + 1, curr, index)
        self.findIslands(grid, islands, row, column - 1, curr, index)
        
        