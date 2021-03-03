class Solution:
    def decodeString(self, s: str) -> str:
        curSting = ''
        curNum = 0
        stack = []
        for char in s:
            if char.isdigit():
                curNum = curNum * 10 + int(char)
            elif char == '[':
                stack.append(curSting)
                stack.append(curNum)
                curSting = ''
                curNum = 0
            elif char == ']':
                preNum = stack.pop()
                preCar = stack.pop()
                curSting = preCar + curSting * preNum
            else:
                curSting += char
        return curSting


"""
"3[a]2[bc]"

make a stack
curSting
curNum
for char in s
if char == dig:
    curNum = curNum *  3 # 有可能是2位數以上
elif char == '[': # 碰到 [ 加入 stack
    stack.append(curSting)
    stack.append(curNum)
    curSting = ''
    curNum = 0
elif char == ']': # 碰到 ] 取出 stack中的上一個Num 與char
    preNum = stack.pop()
    preCar = stack.pop()
    curSting = preCar + curSting*preNum
else:
    curSting += char


    
"""
