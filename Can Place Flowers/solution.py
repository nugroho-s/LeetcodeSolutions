class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        free_space = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and flowerbed[max(i-1, 0)] == 0 and flowerbed[min(i+1, len(flowerbed)-1)] == 0:
                free_space += 1
                flowerbed[i] = 1
        return free_space >= n
