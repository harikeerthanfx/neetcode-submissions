class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")":"(","}":"{","]":"["}

        for ch in s:
            if ch not in match:
                stack.append(ch)
                print(stack)
            else:
                if not len(stack) == 0 and stack[-1] == match[ch]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False
            