class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute force
        # res = []

        # for i in range(len(nums) - k + 1):
        #     maxi = nums[i]
        #     for j in range(i, i+k):
        #         maxi = max(maxi, nums[j])
        #     res.append(maxi)

        # return res

        # Optimal Solution
        res = []
        curr = deque()
        
        for i, n in enumerate(nums):
            while curr and curr[0] <= i-k:
                curr.popleft()
            while curr and nums[curr[-1]] < n:
                curr.pop()
            curr.append(i)
            if i >= k-1:
                res.append(nums[curr[0]])

        return res