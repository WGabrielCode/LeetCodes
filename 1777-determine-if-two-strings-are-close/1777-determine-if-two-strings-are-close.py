class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len( word1 ) != len( word2 ) :
            return False 
        
        from collections import Counter
        
        cnt1 = Counter( word1 ) 
        cnt2 = Counter( word2 ) 
    
        if cnt1.keys() != cnt2.keys() :
            return False 

        if sorted( cnt1.values() ) == sorted( cnt2.values() ) :
            return  True

        return False 
        




