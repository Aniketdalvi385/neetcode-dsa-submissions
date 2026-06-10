class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
        res = 0
        curr = 1
        for i in nums:
            j = i
            while (j+1) in seen:
                curr += 1
                res = max(res, curr)
                j += 1
            curr = 1
            res = max(res, curr)

        return res