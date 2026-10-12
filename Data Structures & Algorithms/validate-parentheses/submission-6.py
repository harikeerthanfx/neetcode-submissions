class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")":"(","}":"{","]":"["}

        for ch in s :
            if ch not in match:
                stack.append(ch)
            else:
                if not stack or  stack[-1] != match[ch]:
                    return False
                
                stack.pop()

        if not stack:
            return True
        else:
            return False
                
