class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len( nums )
        if n < 2 or nums[0] > nums[1] :
            return 0
        if nums[-1] > nums[-2] :
            return n - 1

        nums = [ ( nums,idx) for idx,nums in enumerate( nums ) ]
        
        def quickHighest( A , i  , j ) :
            def partition( A , left , right) : 
                mid  = ( left + right ) // 2 
                i , j = left , right - 1

                A[mid] , A[right] = A[right], A[mid]

                while i <= j :
                    if A[i] > A[right] :
                        A[j] , A[j] = A[i], A[j]
                        j -=1
                    else :
                        i += 1
                
                j += 1
                A[j], A[right] = A[right] , A[j]
                return j

            if i < j :
                pivot_idx = partition( A , i , j )
                quickHighest( A , pivot_idx+1 , j )

        quickHighest( nums , 0 , n-1 )
        return nums[-1][1]