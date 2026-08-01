class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        last_operator = "+"
        n = len(s)

        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)

            if (not char.isdigit() and char != " ") or i == n - 1:
                if last_operator == "+":
                    stack.append(current_number)
                elif last_operator == "-":
                    stack.append(-current_number)
                elif last_operator == "*":
                    stack.append(stack.pop() * current_number)
                elif last_operator == "/":
                    stack.append(int(stack.pop() / current_number))

                last_operator = char
                current_number = 0
        return sum(stack)

