class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
        temp = []
        counter = 0
        
        for char in sentence:
            
            if char not in temp:
                temp.append(char)
                counter += 1
                
            if counter == 26:
                return True
            
        return False
