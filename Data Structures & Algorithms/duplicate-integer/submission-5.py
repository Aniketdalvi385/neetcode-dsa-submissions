class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen: return True
            seen.add(i)

        return False



        # Brute force solution with complexity time: O(n log n) space: O(1) 
        #! Good for space complexity but changes the original array
        # nums.sort()
        # for i, e in enumerate(nums):
        #     if i > 0 and nums[i-1] == nums[i]:
        #         return True

        # return False



