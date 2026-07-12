class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        import heapq

        pq = []

        i = 0 
        length = len( costs )
        j = length - 1

        while i < candidates and i <= j and i < length : 
            heapq.heappush( pq, (costs[i],  i ) )
            i += 1
            if i > j :
                break
            heapq.heappush( pq,( costs[j] , j )  )
            j-=1

        result = 0
        for _ in range( k ) : 
            val, idx =  heapq.heappop(pq)

            result += val
            if i <= j : 
                if idx < i :
                    heapq.heappush( pq, (costs[i], i ) )
                    i += 1 
                else : 
                    heapq.heappush( pq, (costs[j] , j ) )
                    j -= 1  

        return result
            


        
        