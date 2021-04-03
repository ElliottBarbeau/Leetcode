from collections import deque
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s2 = sentence2.split(" ")
        s1 = sentence1.split(" ")
        s1queue = deque()
        s2queue = deque()
        
        for word in s1:
            s1queue.append(word)
            
        for word in s2:
            s2queue.append(word)
            
        while s1queue and s2queue and s1queue[0] == s2queue[0]:
            s1queue.popleft()
            s2queue.popleft()
            
        while s1queue and s2queue and s1queue[-1] == s2queue[-1]:
            s1queue.pop()
            s2queue.pop()
            
        if len(s2queue) == 0 or len(s1queue) == 0:
            return True
        
        return False