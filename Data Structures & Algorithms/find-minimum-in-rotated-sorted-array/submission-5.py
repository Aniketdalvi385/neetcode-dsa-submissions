class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        lo, hi = 0, len(nums)-1

        while lo < hi:
            mid = lo + (hi - lo)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
            
        return nums[lo]