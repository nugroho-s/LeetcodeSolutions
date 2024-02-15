class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                op = stack.pop()
                if (c == ')' and op != '(') or (c == ']' and op != '[') or (c == '}' and op != '{'):
                    return False
        
        return len(stack) == 0