import bisect

class TimeMap:

    def __init__(self):
        
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values_list = self.store[key]
        
        idx = bisect.bisect_right(values_list, (timestamp, chr(127)))
        
        if idx == 0:
            return ""
        
        return values_list[idx - 1][1]
