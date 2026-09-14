class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = "+-*/"
        for i in range(len(tokens)):
            if tokens[i] in operands:
                if tokens[i] == "*":
                    stack.append(stack.pop() * stack.pop())
                elif tokens[i] == "/":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first / second))
                elif tokens[i] == "-":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first - second)
                elif tokens[i] == "+":
                    stack.append(stack.pop() + stack.pop())
            else:    
                stack.append(int(tokens[i]))
        return stack[-1]
