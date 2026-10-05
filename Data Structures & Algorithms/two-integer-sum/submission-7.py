class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
            for p, q in enumerate(nums):
                if i != p and j + q == target:
                    return [i, p]