class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def rec( arr , ltk , n , start_idx, sum_arr ) :

            if sum_arr > n :
                return
            if ltk == 0 and sum_arr == n :
                results.append( arr )
                return

            for i in range( start_idx , 10 ) :
                prev_arr = tuple( arr )
                arr.append( i )
                rec( arr, ltk - 1 , n , i + 1 , sum_arr + i )
                arr = list( prev_arr )
        results = []
        rec( [] , k , n , 1 , 0  )
        return results