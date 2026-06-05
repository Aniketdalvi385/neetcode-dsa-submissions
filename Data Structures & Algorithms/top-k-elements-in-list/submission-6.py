class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force Solution
        # map = {}
        # res = []
        # for i in nums:
        #     map[i] = map.get(i, 0) + 1
        #     if len(res) < k and i not in res:
        #         res.append(i)
        #     elif i not in res:
        #         for ind, j in enumerate(res):
        #             if map[j] < map[i]:
        #                 res[ind] = i
        #                 break
        # return res

        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for item, freq in map.items():
            buckets[freq].append(item)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k : return res