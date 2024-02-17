class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for c in strs[0]:
            for str_val in strs:
                if (i >= len(str_val)) or (str_val[i] != c):
                    return strs[0][:i]
            i = i + 1
        return strs[0]