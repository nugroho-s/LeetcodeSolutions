class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        freq_rank = [] * len(freq_map)
        return [k for k, v in sorted(freq_map.items(), key=lambda item: item[1], reverse=True)][:k]