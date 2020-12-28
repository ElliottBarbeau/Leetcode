class Solution:
    def evalRPN(self, tokens):
        stack = []
        operations = '*+-/'
        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == '+':
                    num1 += num2
                elif token == '-':
                    num1 -= num2
                elif token == '*':
                    num1 *= num2
                elif token == '/':
                    num1 /= num2
                stack.append(num1)
        return int(stack.pop())

print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))