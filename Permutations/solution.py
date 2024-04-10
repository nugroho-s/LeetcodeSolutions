class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) is 1:
            return [nums]
        result = []
        for prev in self.permute(nums[1:]):
            head = nums[0:1]
            for i in range(len(nums)):
                result.append(prev[:i] + head + prev[i:])
        return result
