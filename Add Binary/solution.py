class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        temp = 0
        result = ""
        for i in range(max_len):
            ri = (i+1) * -1
            va = int(a[ri]) if i < len(a) else 0
            vb = int(b[ri]) if i < len(b) else 0
            idx_result = va + vb + temp
            temp = idx_result // 2
            idx_result = idx_result % 2
            result += str(idx_result)
        if temp > 0:
            result += str(temp)
        return result[::-1]
