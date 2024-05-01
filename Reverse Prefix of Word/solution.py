class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        if i > 0:
            return word[i:0:-1] + word[0] + word[i+1:]
        else:
            return word
