class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort( key = lambda x : x[1] )
        cnt =  1
        lt = points[0][1]
        for i in range( 1 , len( points ) ) :
            a , b = points[i]
            if a > lt :
                lt = b 
                cnt += 1
        return cnt