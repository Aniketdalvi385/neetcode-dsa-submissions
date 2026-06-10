class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute force solution this is O(n^2) in worst case.
        # seen = set()
        # for i in nums:
        #     if i not in seen:
        #         seen.add(i)
        # res = 0
        # curr = 1
        # for i in nums:
        #     j = i
        #     while (j+1) in seen:
        #         curr += 1
        #         j += 1
        #     res = max(res, curr)
        #     curr = 1

        # return res

        # Optimal solution pretty close to the Brute force follows the same approach just need additional condition
        # if a there is an element less than n then n is not the begining of the sequence.
        seen = set(nums)
        best = 0

        for n in nums:
            if n-1 not in seen:
                length = 1
                while n+length in seen:
                    length += 1
                best = max(length, best)

        return best