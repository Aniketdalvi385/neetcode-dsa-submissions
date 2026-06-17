class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lsum = [0]*n
        rsum = [0]*n
        res = 0
        for i in range(1,n):
            if height[i-1] >= lsum[i-1]:
                lsum[i] = height[i-1]
            else:
                lsum[i] = lsum[i-1]
            j = (n-1)-i
            if height[j+1] >= rsum[j+1]:
                rsum[j] = height[j+1]
            else: 
                rsum[j] = rsum[j+1]

        for i, j in enumerate(height):
            lmax = lsum[i]
            rmax = rsum[i]
            if lmax < j or rmax < j:
                continue
            depth = min(lmax, rmax)
            res += depth - j

        return res