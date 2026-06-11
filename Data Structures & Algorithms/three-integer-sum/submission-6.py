class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res =set()
        for ind, ele  in enumerate(nums):
            l, r = ind+1, len(nums)-1
            target = -(ele)
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    res.add((ele, nums[l], nums[r]))
                    l += 1
                elif curr > target:
                    r -= 1
                elif curr < target:
                    l += 1
        return [list(t) for t in res]