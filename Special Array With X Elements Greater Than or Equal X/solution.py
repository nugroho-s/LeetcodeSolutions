class Solution:
    def specialArray(self, nums: List[int]) -> int:
        counts = [0] * (len(nums) + 1)
        for num in nums:
            if num < len(nums):
                counts[num] += 1
            else:
                counts[-1] += 1
        for i in range(len(counts)):
            if i == sum(counts[i:]):
                return i
        return -1