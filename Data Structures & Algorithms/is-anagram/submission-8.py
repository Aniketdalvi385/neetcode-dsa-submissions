class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute Force solution complexity: O(n)
        if len(s) != len(t): return False
        map = dict()
        for ch in s:
            map[ch] = map.get(ch, 0) + 1

        for ch1 in t:
            if ch1 not in map or map[ch1] == 0:
                return False
            map[ch1] -= 1
        
        return True

        # Trying with canonical key approach not optimal but fun complexity: O(n log n)
        # if len(s) != len(t): return False
        # skey = sorted(s)
        # tkey = sorted(t)
        # for i, ch in enumerate(skey):
        #     if ch != tkey[i]:
        #         return False
        # return True
