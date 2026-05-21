class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in s:
            if (i=='(' or i=='{' or i=='['):
                a.append(i)
            else:
                if not a:
                    return False
                top = a.pop()
                if (top=='(' and i!=')'):
                    return False
                elif (top=='{' and i!='}'):
                    return False
                elif (top=='[' and i!=']'):
                    return False
        return len(a)==0