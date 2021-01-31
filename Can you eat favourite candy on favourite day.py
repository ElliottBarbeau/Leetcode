class Solution:
    def canEat(self, candiesCount, queries):
        i = 0
        for query in queries:
            favourite_type = query[0]
            favourite_day = query[1]
            daily_cap = query[2]
            while i < len(queries):
                
                