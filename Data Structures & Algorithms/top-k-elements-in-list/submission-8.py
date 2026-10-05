class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for item, freq in map.items():
            buckets[freq].append(item)

        res = []

        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res