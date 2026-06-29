class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        s_map = {}
        t_map = {}
        bestlen, bestleft = float("inf"), 0
        have, need = 0, 0
        
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1
        need = len(t_map)
        
        pt1, pt2 = 0, 0
        while pt2 < len(s):
            right = s[pt2]
            s_map[right] = s_map.get(right, 0) + 1
            if s_map[right] == t_map.get(right, 0):
                have += 1
            while have == need:
                if (pt2 - pt1)+1 < bestlen:
                    bestlen = (pt2 - pt1) + 1
                    bestleft = pt1
                left = s[pt1]
                s_map[left] -= 1
                if s_map[left] < t_map.get(left, 0):
                    have -= 1
                pt1 += 1
            pt2 += 1
        if bestlen == float("inf"):
            return ""
        return s[bestleft:bestleft + bestlen]