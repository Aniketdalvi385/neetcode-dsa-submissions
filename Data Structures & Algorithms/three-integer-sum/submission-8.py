class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res =[]
        for ind, ele  in enumerate(nums):
            if ele > 0:
                break
            if ind > 0 and ele == nums[ind - 1]:
                continue
            l, r = ind+1, len(nums)-1
            target = -(ele)
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    res.append([ele, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif curr > target:
                    r -= 1
                elif curr < target:
                    l += 1
        return res