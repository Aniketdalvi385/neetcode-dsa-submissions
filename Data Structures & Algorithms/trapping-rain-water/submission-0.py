class Solution:
    def trap(self, height: List[int]) -> int:
        lsum = {0: (-1, 0)}
        rsum = {len(height)-1: (-1, 0)}
        res = 0
        for i in range(1,len(height)):
            if height[i-1] >= lsum[i-1][1]:
                lsum[i] = (i-1, height[i-1])
            else:
                lsum[i] = lsum[i-1]
            j = (len(height)-1)-i
            if height[j+1] >= rsum[j+1][1]:
                rsum[j] = (j+1, height[j+1])
            else: 
                rsum[j] = rsum[j+1]

        for i, j in enumerate(height):
            lmax = lsum[i][1]
            rmax = rsum[i][1]
            if lmax < j or rmax < j:
                continue
            depth = min(lmax, rmax)
            res += depth - j

        return res