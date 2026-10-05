class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr = set()
        for i in nums:
            if i in curr:
                return True
            curr.add(i)

        return False