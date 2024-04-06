class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = 0
        result = ""
        for i in range(len(s)):
            result += s[i]
            if s[i] is '(':
                stack += 1
            elif s[i] is ')':
                if stack > 0:
                    stack -= 1
                else:
                    result = result[:-1]
        s = result
        stack = 0
        result = ""
        for j in range(len(s)):
            i = len(s) - j - 1
            result = s[i] + result
            if s[i] is ')':
                stack += 1
            elif s[i] is '(':
                if stack > 0:
                    stack -= 1
                else:
                    result = result[1:]
        return result
