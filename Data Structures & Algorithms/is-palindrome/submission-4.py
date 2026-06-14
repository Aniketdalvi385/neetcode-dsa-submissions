class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Brute Force with two pointers. Approach is optimal but needs little cleanup.
        # start = 0
        # end = len(s) - 1
        # while end > start:
        #     if s[start].isalnum() == False:
        #         while s[start].isalnum() == False and start < end:
        #             start += 1
        #     if s[end].isalnum() == False:
        #         while s[end].isalnum() == False and end > start:
        #             end -= 1
        #     if s[start].lower() != s[end].lower():
        #             return False
        #     start += 1
        #     end -= 1
            
        # return True

        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True