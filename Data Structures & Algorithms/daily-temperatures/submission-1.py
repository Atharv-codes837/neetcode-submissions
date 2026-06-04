class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        n = len(temperatures)
        res = [0]*n
        for i,t in enumerate(temperatures):
            while s and t>s[-1][0]:
                sTemp,sIdx = s.pop()
                res[sIdx] = i-sIdx
            s.append((t,i))
        return res

            
        