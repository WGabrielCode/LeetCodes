class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort( key = lambda x : (x[1],x[0]) )
        cnt =  0
        inf = -float( "inf" )
        start , end = inf , inf 
        for a , b  in intervals :
            if a < end or b <= end :
                cnt += 1
            else :
                start , end = a , b
        return cnt