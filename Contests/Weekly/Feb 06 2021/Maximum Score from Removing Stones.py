'''
You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. 
Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score.
The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.
'''
class Solution:
    def maximumScore(self, a, b, c):
        arr = sorted([a, b, c])
        count = 0
        while arr[0] > 0:
            if b > c:
                arr[1], arr[2] = arr[2], arr[1]
            arr[0] -= 1
            arr[2] -= 1
            count += 1

        count += min(arr[1], arr[2])

        return count