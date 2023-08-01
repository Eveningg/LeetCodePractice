class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #test = str(x)
        newStr = str(x)[::-1]
        if str(x) == newStr:
            return(True)

        else:
            return(False)