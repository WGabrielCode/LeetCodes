class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_k( k ) :
            cnt = 0 
            for num in piles : 
                cnt += ( num + k - 1) // k #+ ( 0 if num % k == 0 else 1  )
                if cnt > h :
                    return False
            return True 


        left = 1
        right = max( piles ) 

        while( left < right ) :
            mid = ( left + right ) // 2
            if check_k( mid ) :
            
                right = mid
            else :
                left = mid + 1

        return left




            