class Solution:
    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
        i = 0
        while i < len(restaurants):
            if restaurants[i][3] > maxPrice or restaurants[i][4] > maxDistance or (veganFriendly and not restaurants[i][2]):
                restaurants.pop(i)
            else:
                i += 1
                
        restaurants = sorted(restaurants, key = lambda x: (x[1], x[0]))[::-1]
        
        ret = []
        for num in restaurants:
            ret.append(num[0])
            
        return ret