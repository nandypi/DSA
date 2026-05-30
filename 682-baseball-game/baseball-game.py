class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "C":
                stack = stack[:-1]
            elif i == "D":
                prev = stack[-1]
                stack.append(prev*2)
            elif i == "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
