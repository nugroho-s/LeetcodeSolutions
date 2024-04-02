class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        reverse_map = {}
        for i in range(len(s)):
            if s[i] in char_map:
                if t[i] not in reverse_map:
                    return False
                else:
                    if char_map[s[i]] is not t[i] or reverse_map[t[i]] is not s[i]:
                        return False
            elif t[i] in reverse_map:
                return False
            else:
                char_map[s[i]] = t[i]
                reverse_map[t[i]] = s[i]
        return True