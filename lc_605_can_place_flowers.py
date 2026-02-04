class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        flowerbed.append(0)
        for i in range(len(flowerbed)-1):
            if flowerbed[i] == 0 and prev == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1

            prev = flowerbed[i]
        return 0 >= n
