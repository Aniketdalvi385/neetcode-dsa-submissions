class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen = {}
        for i, j in enumerate(nums):
            if (target - j) in nums:
                if nums.index(target - j) < i:
                    return [nums.index(target - j), i]
        return[]