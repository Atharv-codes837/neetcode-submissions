class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        m = len(matrix)
        n = len(matrix[0])
        end = n-1
        for row in range(m):
            if(target>=matrix[row][0] and target<=matrix[row][end]):
                break
        l = 0
        r = n-1
        while(l<=r):
            m = l+(r-l)//2
            if target==matrix[row][m]:
                return True
            elif target<matrix[row][m]:
                r = m-1
            else:
                l = m+1
        return False

        


        