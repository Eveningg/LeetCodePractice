class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Two Hashmaps Solution
        
        # Checking Strings are same length.
        if len(s) != len(t):
            return False
            
        countS, countT = {}, {}
        
        for i in range(len(s)):
            
            # hashmap index i of string s equals 1 + the current num at that index
            # if index doesn't exist, uses default value set to 0
            countS[s[i]] = 1 + countS.get((s[i]), 0)
            countT[t[i]] = 1 + countT.get((t[i]), 0)
            
        # Comparing Key Length For Each Index, If Not Equal, It Is Not An Anagram
        for char in countS:
            if countS[char] != countT.get(char, 0):
                return False
            
        return True
            