class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = -1
        start = -1
        i = len(s) - 1
        while s[i] is " ":
            i -= 1
        end = i
        while s[i] is not " " and i >= 0:
            i -= 1
        start = i
        return end-start