class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]):
        d = {}
        res = []
        for pair in adjacentPairs:
            if pair[0] not in d:
                d[pair[0]] = []
            d[pair[0]].append(pair[1])
            if pair[1] not in d:
                d[pair[1]] = []
            d[pair[1]].append(pair[0])
            
        start = -123123123
        for pair in adjacentPairs:
            for val in pair:
                if len(d[val]) == 1:
                    start = val
                    
        if start == -123123123:
            return []
        
        while len(res) < len(d.keys()):
            res.append(start)
            for val in d[start]:
                if val not in res:
                    start = val
                    print(start)
                    continue
                        
        return res