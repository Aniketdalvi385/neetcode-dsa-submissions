class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pt1, pt2 = 0, 1 
        res = 0
        seen = {}
        seen[s[pt1]] = 1
        hi, total = 1, 1
        while pt2 < len(s):
            seen[s[pt2]] = seen.get(s[pt2], 0) + 1
            hi = max(seen[s[pt2]], hi)
            total += 1
            while total-hi > k:
                seen[s[pt1]] -= 1
                pt1 += 1
                total -= 1
            
            res = max(total, res)
            pt2 += 1

        return res

