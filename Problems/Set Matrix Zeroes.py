class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = [1] * len(matrix)
        columns = [1] * len(matrix[0])

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    rows[row] = 0
                    columns[column] = 0

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if rows[row] == 0 or columns[column] == 0:
                    matrix[row][column] = 0