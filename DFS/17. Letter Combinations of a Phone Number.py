class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        code = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}

        answer = []

        def track(word, next_dig):
            # check dig是否有輸入，沒有則直接回傳目前word
            if len(next_dig) == 0:
                answer.append(word)
            else:
                for letter in code[next_dig[0]]:
                    # 將目前字母加入傳入的word，並繼續下一個傳入數字的搜尋
                    track(word+letter, next_dig[1:])

        # 傳入的有內容
        if digits:
            # 開始track搜尋
            track("", digits)
        # 最後return answer
        return answer
