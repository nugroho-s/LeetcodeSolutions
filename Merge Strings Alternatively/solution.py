class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        result = ""
        for i in range(min_len):
            result += word1[i]
            result += word2[i]
        result += word1[min_len:]
        result += word2[min_len:]
        return result
