class Solution:
    phone = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is "":
            return ""
        if len(digits) is 1:
            return list(self.phone[int(digits[0])-2])
        else:
            first_chars = list(self.phone[int(digits[0])-2])
            remainders = self.letterCombinations(digits[1:])
            result = []
            for c in first_chars:
                for r in remainders:
                    result.append(c+r)
            return result
