class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate(nums):
            if (target - j) in seen:
                if seen[target - j] < i:
                    return [seen[target - j], i]
            seen[j] = i
        return[]