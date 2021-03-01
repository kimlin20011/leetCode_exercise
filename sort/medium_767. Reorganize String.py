class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = collections.Counter(S)　  # 使用python counter api，計算每個字串出現的次數
        ans = "#"  # 先設第一個數為#
        while counter:
            stop = True
            for item, times in counter.most_common():  # counter有東西但是都沒有加到
                if ans[-1] != item:  # 如果新的item不能與舊的最後一個item
                    ans += item
                    counter[item] -= 1
                    if not counter[item]:  # 如果counter item數為0，刪除 counter
                        del counter[item]
                    stop = False
                    break  # 有加進去，跳出從來
            if stop:  # 如果只有counter只有一個數，上面for loop中的if就沒辦法進去，於是為impossible，所以直接跳出
                break
        return ans[1:] if len(ans) == len(S) + 1 else ""  # 輸出anser從1之後的字串
