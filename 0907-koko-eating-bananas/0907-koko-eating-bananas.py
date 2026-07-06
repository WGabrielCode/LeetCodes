class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        def check_k( k ) :
            cnt = 0 
            for num in piles : 
                cnt += ( num + k - 1) // k
                if cnt > h :
                    return False
            return True 

        if len( piles ) == h :
            return max( piles )

        left = ( sum( piles) + h -1 ) // h 
        right = max( piles ) 

        while( left < right ) :
            mid = ( left + right ) // 2
            if check_k( mid ) :
            
                right = mid
            else :
                left = mid + 1

        return left




            