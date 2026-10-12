class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = []
        ops = ["+","-","/","*"]

        for ch in tokens:
            if ch in ops:
                b = int(stack.pop())
                a = int(stack.pop())
                if ch == "+":
                    stack.append(a+b)
                elif ch == "-":
                    stack.append(a-b)
                elif ch == "/":
                    stack.append(a/b)
                else:
                    stack.append(a*b)
            else:
                stack.append(ch)            
        
        return int(stack[0])