class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for ind1, i in enumerate(nums):
            curr = 1
            for ind2, j in enumerate(nums):
                if ind1 != ind2:
                    curr *= j
            res.append(curr)
        return res