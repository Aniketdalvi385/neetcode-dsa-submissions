class Solution:
    @staticmethod
    def validSub(s_map: dict, t_map: dict) -> bool:
        for ch in t_map.keys():
            if t_map[ch] > s_map.get(ch, 0):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        s_map = {}
        t_map = {}
        res = ""
        
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1
        
        pt1, pt2 = 0, 0
        while pt2 < len(s):
            s_map[s[pt2]] = s_map.get(s[pt2], 0) + 1
            while self.validSub(s_map, t_map):
                curr = s[pt1: pt2+1]
                if res == "" or len(res) > len(curr):
                    res = curr
                s_map[s[pt1]] -= 1
                pt1 += 1
            pt2 += 1
        return res