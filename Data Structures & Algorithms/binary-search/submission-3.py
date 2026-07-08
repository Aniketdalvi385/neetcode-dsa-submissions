class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute force Binary search approach Time Complexity: O(log n) Space Complexity: O(1)
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
            
        return -1