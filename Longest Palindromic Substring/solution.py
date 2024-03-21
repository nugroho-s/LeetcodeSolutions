class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        longest_size = 1
        longest_sub_str = s[0:1]
        for i in range(len(s)):
            if i + longest_size >= len(s):
                break
            for j in range(len(s), i+longest_size, -1):
                sub_str = (s[i:j])
                if self.isPalindrome(sub_str):
                    longest_size = len(sub_str)
                    longest_sub_str = sub_str
                    break
        return longest_sub_str
