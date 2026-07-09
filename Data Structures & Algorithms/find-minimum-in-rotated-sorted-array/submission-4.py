class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        else:
            l, r = 0, len(nums)-1
            curr = nums[-1]
            while l <= r:
                mid = l + (r - l)//2
                print(nums[l], nums[mid], nums[r])
                if nums[mid] > nums[l]:
                    l = mid
                else:
                    r = mid - 1
                curr = min(nums[mid], curr, nums[l], nums[r])

            return curr