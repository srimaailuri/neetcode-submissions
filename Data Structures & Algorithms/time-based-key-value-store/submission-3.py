class TimeMap:

    def __init__(self):
        self.time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = []

        self.time[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""

        data = self.time[key]
        left = 0
        right = len(data) - 1
        answer = ""

        while left <= right:
            mid = (left + right) // 2

            if data[mid][0] <= timestamp:
                answer = data[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return answer