class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix) * len(matrix[0])
        res = []
        
        top_row = 0
        right_column = len(matrix[0]) - 1
        bottom_row = len(matrix) - 1
        left_column = 0
        
        while len(res) < n:
            
            for i in range(left_column, right_column + 1):
                res.append(matrix[top_row][i])
            top_row += 1
                
            if len(res) == n:
                break

            for i in range(top_row, bottom_row + 1):
                res.append(matrix[i][right_column])
            right_column -= 1

            if len(res) == n:
                break
                
            i = right_column
            while i >= left_column:
                res.append(matrix[bottom_row][i])
                i -= 1
            bottom_row -= 1
                
            if len(res) == n:
                break
            
            i = bottom_row
            while i >= top_row:
                res.append(matrix[i][left_column])
                i -= 1
            left_column += 1
            
                
        return res

print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))