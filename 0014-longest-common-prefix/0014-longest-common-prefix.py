class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        result = ""
        
        # Iterating Code The Number Of Times Equal To First String Length of list "str"
        for i in range(len(strs[0])):

            # Iterating Through Every String In List "Str"
            for string in strs:
                
                # If "I" equal to length of string being read, or if Character I Not Equal To Characters At Same Index Of Other Strings, Return Result
                # If First Condition Is True, Other Result Not Read
                if i == len(string) or string[i] != strs[0][i]:
                    return result
            
            result += strs[0][i]
            
        return result
                

        