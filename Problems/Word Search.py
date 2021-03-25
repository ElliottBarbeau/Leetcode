from copy import deepcopy, copy
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0] and self.dfs(board, word, 0, row, column):
                    return True
                
        return False
                
    def dfs(self, board, word, index, row, column):
        if index == len(word):
            return True
        if row >= len(board) or column >= len(board[0]) or row < 0 or column < 0 or board[row][column] != word[index]:
            return False            
        board[row][column] = "*"
        
        if self.dfs(board, word, index + 1, row + 1, column) or \
            self.dfs(board, word, index + 1, row - 1, column) or \
            self.dfs(board, word, index + 1, row, column + 1) or \
            self.dfs(board, word, index + 1, row, column - 1):
            return True

        board[row][column] = word[index]
        return False
            

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(Solution().exist(board, word))