class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        seen = set()
        self.jump(arr, start, seen)
        for num in arr:
            if num == float('inf'):
                return True

        return False

    def jump(self, arr, index, seen):
        if index in seen or arr[index] == float('inf'):
            return
        seen.add(index)

        if arr[index] == 0:
            arr[index] = float('inf')
            return

        if index + arr[index] < len(arr):
            self.jump(arr, index + arr[index], seen)
        
        if index - arr[index] >= 0:
            self.jump(arr, index - arr[index], seen)
            