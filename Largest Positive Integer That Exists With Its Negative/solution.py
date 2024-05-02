class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_map = set()
        max_num = -1
        for num in nums:
            if abs(num) > max_num and (num * -1) in num_map:
                max_num = abs(num)
            num_map.add(num)
        return max_num
