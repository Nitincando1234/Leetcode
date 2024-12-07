class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        value, n = 0, len(s)
        sign = "+"
        for i, char in enumerate(s):
            if char.isdigit():
                value = value * 10 + int(char)
            if i == n - 1 or char in "+-/*":
                if sign == "+":
                    stack.append(value)
                elif sign == "-":
                    stack.append(-value)
                elif sign == "*":
                    stack.append(stack.pop() * value)
                elif sign == "/":
                    stack.append(int(stack.pop() / value))
                sign = char
                value = 0
        return sum(stack)            