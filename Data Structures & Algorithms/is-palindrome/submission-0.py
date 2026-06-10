class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while end > start:
            if s[start].isalnum() == False:
                while s[start].isalnum() == False and start < end:
                    start += 1
            if s[end].isalnum() == False:
                while s[end].isalnum() == False and end > start:
                    end -= 1
            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() != s[end].lower():
                    return False
            start += 1
            end -= 1
            
        return True