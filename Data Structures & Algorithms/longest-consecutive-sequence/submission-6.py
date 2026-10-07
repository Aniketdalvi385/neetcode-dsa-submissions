class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        seen = set(nums)

        for i in nums:
            if i-1 not in seen:
                length = 1
                while i+length in seen:
                    length += 1
                best = max(length, best)
            
        return best