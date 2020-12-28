from collections import deque
class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        ps = queue.popleft()
        if ps.openCount == num and ps.openCount == ps.closeCount:
            result.append(ps.str)
        else:
            if ps.openCount < num:
                queue.append(ParenthesesString(ps.str + '(', ps.openCount + 1, ps.closeCount))
            if ps.closeCount < ps.openCount:
                queue.append(ParenthesesString(ps.str + ')', ps.openCount, ps.closeCount + 1))

    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
