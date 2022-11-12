from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        self.data = SortedList()

    def add_num(self, num: int) -> None:
        self.data.add(num)

    def find_median(self) -> float:
        n = len(self.data)
        return (self.data[n//2] + self.data[(n-1)//2]) / 2


obj = MedianFinder()
obj.add_num(1)
obj.add_num(2)
print(obj.find_median())

