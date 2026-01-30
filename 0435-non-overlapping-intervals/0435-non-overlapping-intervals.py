class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        length = len( intervals ) 
        if length <= 1 :
            return 0

        intervals.sort( key = lambda x : x[1] )
        cnt =  0
        end = intervals[0][1]
        for idx in range( 1 , len( intervals ) ) :
            a , b = intervals[idx]
            if a < end:
                cnt += 1
            else :
                end = b
        return cnt