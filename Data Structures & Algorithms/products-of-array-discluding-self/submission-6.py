class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        run = []
        curr = 1
        for num in nums:
            run.append(curr)
            curr *= num

        res = [1 for i in range(len(nums))]
        curr = 1
        for i in range(len(nums)-1, -1 , -1):
            res[i] = curr*run[i]
            curr *= nums[i]
        return res