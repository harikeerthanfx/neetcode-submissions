class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = []
        for x in tokens:
            if x.lstrip('+-').isdigit():
                stack.append(int(x))
            else:
                if x=='+':
                    b=stack.pop()
                    a=stack.pop()
                    stack.append(a+b)
                elif x=='-':
                    b=stack.pop()
                    a=stack.pop()
                    stack.append(a-b)
                elif x=='*':
                    b=stack.pop()
                    a=stack.pop()
                    stack.append(a*b)
                elif x=='/':
                    b=stack.pop()
                    a=stack.pop()
                    stack.append(int(a/b))
                else:
                    print("Invalid")
        return stack[0]
                