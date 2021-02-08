from copy import deepcopy
class Solution:
    def prisonAfterNDays(self, cells, N):
        
        newarray = deepcopy(cells)
        for _ in range(N):
            for j in range(1, len(cells)-1):
                if j == 0 or j == len(cells) - 1:
                    newarray[j] = 0
                else:
                    if (cells[j - 1] == 0 and cells[j + 1] == 0) or (cells[j - 1] == 1 and cells[j + 1] == 1):
                        newarray[j] = 1
                    else:
                        newarray[j] = 0
            cells = deepcopy(newarray)
            
        return cells

print(Solution().prisonAfterNDays([0,1,0,1,1,0,0,1], 7))
print(Solution().prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))