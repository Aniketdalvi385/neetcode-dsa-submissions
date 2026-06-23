class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        point1, point2 = 0, 0
        res = 0
        seen = set()
        while point2 < len(s):
            while s[point2] in seen:
                seen.remove(s[point1])
                point1 += 1
            seen.add(s[point2])
            res = max((point2 - point1)+1, res)
            point2 += 1

        return res