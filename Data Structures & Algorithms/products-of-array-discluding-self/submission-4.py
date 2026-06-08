class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force with O(n^2) Complexity not good at all
        # res = []
        # for ind1, i in enumerate(nums):
        #     curr = 1
        #     for ind2, j in enumerate(nums):
        #         if ind1 != ind2:
        #             curr *= j
        #     res.append(curr)
        # return res

        # Second approach like a Running sum but still around O(n^2)
        # curr = 1
        # res = []
        # for ind, ele in enumerate(nums):
        #     total = curr
        #     for i in range(ind+1, len(nums)):
        #         total *= nums[i]
        #     res.append(total)
        #     curr *= ele

        # return res

        # Optimal approach with time complexity: O(n) and space complexity: O(n)
        # n = len(nums)
        # prefix = [1] * n
        # suffix = [1] * n

        # for i in range(1, n):
        #     prefix[i] = prefix[i-1] * nums[i-1]

        # for i in range(n-2, -1, -1):
        #     suffix[i] = suffix[i+1] * nums[i+1]

        # return [prefix[i] * suffix[i] for i in range(n)]

        # Another Version of Optimal Approach with space complexity reduced to O(1)
        n = len(nums)
        res = [1] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
