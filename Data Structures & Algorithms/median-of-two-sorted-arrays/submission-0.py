class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        arr = sorted(nums1+nums2)
        print(arr)

        if len(arr)%2 == 1:
            mid = len(arr)//2
            print(arr[mid])
            return arr[mid]
        else:
            mid = len(arr)//2
            print(arr[mid-1], arr[mid])
            return (arr[mid-1] + arr[mid])/2