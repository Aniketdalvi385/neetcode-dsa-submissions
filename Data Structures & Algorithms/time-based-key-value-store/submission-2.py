class TimeMap:
    # Single Dict Solution
    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap.get(key, [])
        lo, hi = 0, len(arr)-1
        lastValid = (-1, '')

        while lo <= hi:
            mid = lo + (hi - lo)//2
            if arr[mid][0] <= timestamp:
                lastValid = arr[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lastValid[1]