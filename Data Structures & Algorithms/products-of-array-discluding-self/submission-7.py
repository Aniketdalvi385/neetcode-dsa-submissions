class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        curr = 1
        for num in nums:
            res.append(curr)
            curr *= num

        curr = 1
        for i in range(len(nums)-1, -1 , -1):
            res[i] = curr*res[i]
            curr *= nums[i]
        return res