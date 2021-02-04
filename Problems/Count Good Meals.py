from math import pow

class Solution:
    def countPairs(self, deliciousness):
        d = {}
        for i in range(len(deliciousness)):
            if deliciousness[i] not in d:
                d[deliciousness[i]] = 0
            d[deliciousness[i]] += 1

        deliciousness.sort(reverse = True)
        result = 0
        for i in range(len(deliciousness)):
            if(d[deliciousness[i]] < 1):
                continue

            print(deliciousness, deliciousness[i])

            current = 1
            while (current <= pow(2, 20)):
                current = current << 1
                print(current, result, deliciousness, deliciousness[i])

                if (current - deliciousness[i]) in d.keys():
                    if (current - deliciousness[i] == deliciousness[i] and d[deliciousness[i]] == 1):
                        continue
                    
                    result += 1

        return result

print(Solution().countPairs([1,1,1,3,3,3,7]))