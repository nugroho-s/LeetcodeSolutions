class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while k > 0 and stack and stack[-1] > num[i]:
                popped = stack.pop()
                k = k-1
            stack.append(num[i])
        while stack and k > 0:
            k -= 1
            stack.pop()
        stack = "".join(stack).lstrip("0")
        return stack if stack else "0"
