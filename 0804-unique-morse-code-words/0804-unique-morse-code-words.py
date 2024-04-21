class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        

        morseCodeDict   = { 'A':'.-', 'B':'-...',
                            'C':'-.-.', 'D':'-..', 'E':'.',
                            'F':'..-.', 'G':'--.', 'H':'....',
                            'I':'..', 'J':'.---', 'K':'-.-',
                            'L':'.-..', 'M':'--', 'N':'-.',
                            'O':'---', 'P':'.--.', 'Q':'--.-',
                            'R':'.-.', 'S':'...', 'T':'-',
                            'U':'..-', 'V':'...-', 'W':'.--',
                            'X':'-..-', 'Y':'-.--', 'Z':'--..' }

        morseCode = []

        for word in words:
            string = ''
            for char in word:
                string += morseCodeDict[char.upper()]

            morseCode.append(string)


        
        return len(set(morseCode))
    