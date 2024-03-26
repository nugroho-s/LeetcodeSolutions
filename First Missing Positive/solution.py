class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # negative number doesn't matter, so we change it to n+1 so
        # that it wont interfere with our mark
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        # mark num present by changing array on index num
        for i in range(n):
            num = abs(nums[i])
            if num <= n and nums[num-1] > 0:
                nums[num-1] *= -1
        
        # search for unmarked value (positive value), 
        # return n+1 if doesn't exist
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
