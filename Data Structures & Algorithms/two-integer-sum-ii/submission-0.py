class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        n = len(nums)
        j = n-1
        while(i<j):
            if target == (nums[i] + nums[j]):
                return [i+1,j+1]
            elif target > nums[i] + nums[j]:
                i+=1
            else:
                j-=1
        return []

        