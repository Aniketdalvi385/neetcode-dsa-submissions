class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res =[]
        for ind, ele  in enumerate(nums):
            l, r = ind+1, len(nums)-1
            target = -(ele)
            seen = ele
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    new = [ele, nums[l], nums[r]]
                    if not new in res:
                        res.append([ele, nums[l], nums[r]])
                    l += 1
                elif curr > target:
                    currr = nums[r]
                    while nums[r] == currr and l < r:
                        r -= 1
                elif curr < target:
                    currl = nums[l]
                    while nums[l] == currl and l < r:
                        l += 1
        return res