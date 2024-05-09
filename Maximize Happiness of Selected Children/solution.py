class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        result = 0
        for i in range(k):
            happy = max(happiness.pop() - i, 0)
            result += happy
        return result