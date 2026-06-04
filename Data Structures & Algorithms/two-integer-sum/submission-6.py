class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force solution with a hashmap (Actually is optimal)
        seen = {}
        for i, j in enumerate(nums):
            if (target - j) in seen:
                return [seen[target - j], i]
            seen[j] = i
        return[]

        # Thought this is optimal but the existance check and index finding is O(n) each in worst case they can be O(n^2)
        # for i, j in enumerate(nums):
        #     if (target - j) in nums:   # this one 
        #         if nums.index(target - j) < i:    # this one
        #             return [nums.index(target - j), i]
        # return[]