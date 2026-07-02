class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 2 or nums[0] > nums[1] :
            return 0
        if nums[-1] > nums[-2] :
            return len(nums) - 1
        
        nums = sorted( [ (idx,num ) for idx ,num in enumerate( nums )] , key = lambda x : x[1] )

        return nums[-1][0]