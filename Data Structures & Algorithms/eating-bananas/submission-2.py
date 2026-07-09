class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxB = 0
        for i in piles:
            maxB = max(maxB, i)
        
        lo, hi = 1, maxB

        lastValid = hi
        
        while lo <= hi:
            mid = lo + (hi - lo)//2
            count = 0
            for i in piles:
                if i < mid:
                    count += 1
                else:
                    count += math.ceil(i/mid)
            if count <= h:
                lastValid = mid
                hi = mid - 1
            else: 
                lo = mid + 1

        return lastValid