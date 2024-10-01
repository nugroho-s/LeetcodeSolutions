class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modulo_arr = [0] * k
        for i in arr:
            modulo_arr[i % k] += 1
        for i in range(1, k // 2 + 1):
            if modulo_arr[i] != modulo_arr[k-i]:
                return False
        return modulo_arr[0] % 2 == 0