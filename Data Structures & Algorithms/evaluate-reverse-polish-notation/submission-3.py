class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i=='+':
                b = int(s.pop())
                a = int(s.pop())
                s.append(a+b)
            elif i=='-':
                b = int(s.pop())
                a = int(s.pop())
                s.append(a-b)
            elif i=='*':
                b = int(s.pop())
                a = int(s.pop())
                s.append(a*b)
            elif i=='/':
                b = int(s.pop())
                a = int(s.pop())
                if b!=0:
                    s.append(a/b)
            else:
                s.append(i)
        return int(s[0])
        