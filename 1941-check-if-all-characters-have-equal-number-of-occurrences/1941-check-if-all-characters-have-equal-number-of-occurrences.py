class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        amount = s.count(s[0])
        for i in s:
            if s.count(i) != amount:
                return False
        
        return True
