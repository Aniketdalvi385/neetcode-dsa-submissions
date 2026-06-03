class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        validChar = {}
        for ch in s:
            validChar[ch] = validChar.get(ch, 0) + 1

        for ch in t:
            if ch not in validChar:
                return False
            validChar[ch] -= 1
            if validChar[ch] < 0:
                return False
        
        return True
        