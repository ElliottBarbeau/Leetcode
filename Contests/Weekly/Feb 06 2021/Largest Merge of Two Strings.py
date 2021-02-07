# This solution looks really bad and can very likely be improved on
class Solution:
    def largestMerge(self, word1, word2):
        
        def helper(word1, word2):
            if word1 == '':
                if word2 == '':
                    return ''
                else:
                    return word2

            elif word2 == '':
                return word1
            

            if word1[0] == word2[0]:
                word1_index, word2_index = 0, 0
                while word1[word1_index] == word2[word2_index] and word1_index < len(word1) - 1 and word2_index < len(word2) - 1:
                    word1_index += 1
                    word2_index += 1

                if word1[word1_index] > word2[word2_index]:
                    return word1[0] + helper(word1[1:], word2)
                elif word1[word1_index] < word2[word2_index]:
                    return word2[0] + helper(word1, word2[1:])
                else:
                    if len(word2) > len(word1):
                        return word2[0] + helper(word1, word2[1:])
                    else:
                        return word1[0] + helper(word1[1:], word2)
            elif word1[0] > word2[0]:
                return word1[0] + helper(word1[1:], word2)
            else:
                return word2[0] + helper(word1, word2[1:])

        return helper(word1, word2)

print(Solution().largestMerge('cabaa', 'bcaaa'))
print(Solution().largestMerge('abcabc', 'abdcaba'))
print(Solution().largestMerge("nnnnpnnennenpnnnnneenpnn", "nnnennnnnnpnnennnnennnnee"))