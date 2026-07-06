class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len( piles ) == h :
            return max( piles )

        left = 1
        right = max( piles ) 

        while( left < right ) :
            mid  = ( left + right ) // 2
            if sum( [math.ceil( num / mid ) for num in piles] ) <= h :
                right = mid
            else :
                left = mid + 1

        return left




            