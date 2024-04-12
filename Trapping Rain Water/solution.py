class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = [0] * len(height), [0] * len(height)
        max_left[0] = height[0]
        max_right[len(height) - 1] = height[len(height) - 1]

        i, j = 1, len(height) - 2
        while i < len(height):
            max_left[i] = max(max_left[i-1], height[i])
            max_right[j] = max(max_right[j+1], height[j])
            i += 1
            j -= 1

        water = 0
        for i in range(len(height)):
            water += max(min(max_left[i], max_right[i]) - height[i], 0)
        
        return water
