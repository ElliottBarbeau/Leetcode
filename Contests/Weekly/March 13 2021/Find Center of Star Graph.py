from collections import defaultdict
class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        d = defaultdict(list)
        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])

            if len(d[edge[0]]) == len(edges) - 1:
                return edge[0]

            if len(d[edge[1]]) == len(edges) - 1:
                return edge[1]

edges = [[1,2],[2,3],[4,2]]
print(Solution().findCenter(edges))