from collections import deque
class Solution:
    def countStudents(self, students, sandwiches) -> int:
        stack = sandwiches[::-1]
        queue = deque()
        for student in students:
            queue.appendleft(student)
            
        count = len(queue)
        while queue and count >= 0:
            if not stack:
                return len(queue)
            if queue[-1] == stack[-1]:
                queue.pop()
                stack.pop()
                count = len(queue)
            else:
                student = queue.pop()
                queue.appendleft(student)
                count -= 1
                
        return len(queue)

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(Solution().countStudents(students, sandwiches))