class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute Force solution 
        if len(s) != len(t): return False
        map = dict()
        for ch in s:
            map[ch] = map.get(ch, 0) + 1

        for ch1 in t:
            if ch1 not in map or map[ch1] < 0:
                return False
            map[ch1] -= 1
        
        for j in map.values():
            if j > 0:
                return False
        
        return True

        