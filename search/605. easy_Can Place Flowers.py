class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerAvailalbe = 0
        # 第一個與最後一個數也可以放花，在追第一個數的時候，-1會直接讀取最後一個數，所以直接在最後面加2個0
        # [1,0,0,0,1] => [0,1,0,0,0,1,0] => [1,0,0,0,1,0,0]
        flowerbed.extend([0, 0])
        # 判斷每個花盆是否空（= 0），且前面一個與後面一個是不是空，若成立，則可放花（+1）
        # 遍歷到倒數第三個數，因為最後一個數應該是要擺在第一位的花盆
        for i in range(len(flowerbed)-2):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                flowerAvailalbe += 1
        # 最後，判斷可以放花的盆子是否大於題目要求（n）
        return flowerAvailalbe >= n
