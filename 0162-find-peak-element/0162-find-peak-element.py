class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def rec( A , i , j ) : 
            while i != j :
                mid = ( i + j ) // 2
                if A[mid + 1] > A[mid] :
                    i = mid + 1
                else :
                    j = mid
            return i

        n = len( nums )
        return rec(nums , 0 , n-1 ) 

