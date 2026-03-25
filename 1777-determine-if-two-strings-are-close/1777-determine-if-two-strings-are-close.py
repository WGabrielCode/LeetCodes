class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len( word1 ) != len( word2 ) :
            return False 
        
        s1 , s2 = set( word1 ) , set( word2 )
        
        if s1 != s2  :
            return False 
        
        cnt1 = {}
        for char1 in word1 :
            if not char1 in cnt1 :
                cnt1[char1] = 1
            else :
                cnt1[char1] += 1

        cnt2 = {}
        for char2 in word2 :
            if not char2 in cnt2 :
                cnt2[char2] = 1
            else :
                cnt2[char2] += 1
        
        if sorted( cnt1.values() ) == sorted( cnt2.values() ) :
            return  True # sorted( cnt1.values() ) , sorted( cnt2.values() )

        return False 
        




