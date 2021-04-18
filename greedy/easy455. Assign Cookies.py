class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) == 0 or len(s) == 0:
            return 0
        g, s = sorted(g), sorted(s)
        count = 0
        s_pointer, g_pointer = len(s) - 1, len(g) - 1
        while s_pointer >= 0 and g_pointer >= 0:
            if g[g_pointer] <= s[s_pointer]:
                count += 1
                s_pointer -= 1
            g_pointer -= 1
        return count

        # 用greed
        # 先排序2個array
        # 從最後面的index開始比較大小
        # 如果s比g大，那就代表可以給孩子
        # 反之則無法滿足目前最大需求的孩子，直接跳過並看下個孩子
        # 例如：
        # g = [3,4,5,7]
        # s = [1,1,9,10]
