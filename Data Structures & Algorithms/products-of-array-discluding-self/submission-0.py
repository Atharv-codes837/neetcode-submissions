class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_product = 1
        n = len(nums)
        res = [0]*n
        res[0] = 1
        for i in range(1,n):
            res[i] = res[i-1]*nums[i-1]
        r = n-1
        while(r>=0):
            res[r]  = res[r]*right_product
            right_product *= nums[r]
            r-=1
        return res




        
        