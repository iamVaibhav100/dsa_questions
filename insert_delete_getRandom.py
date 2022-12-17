import random


# Using set
class RandomizedSet:
    def __init__(self):
        self.set = set()
        self.list = []

    def insert(self, val):
        if val in self.set:
            return False
        else:
            self.set.add(val)
            self.list.append(val)
            return True

    def remove(self, val):
        if val not in self.set:
            return False
        else:
            self.set.remove(val)
            self.list.remove(val)
            return True

    def get_random(self):
        return random.choice(self.list)

    def __str__(self):
        return str(self.list)


# using hashmap
class RandomizedSet2:
    def __init__(self):
        self.arr = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.arr.append(val)
        self.indices[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        i = self.indices[val]
        self.indices[self.arr[-1]] = i
        self.arr[i] = self.arr[-1]
        self.arr.pop()
        self.indices.pop(val)
        return True

    def get_random(self) -> int:
        return random.choice(self.arr)


if __name__ == "__main__":
    random_set1 = RandomizedSet()
    random_set2 = RandomizedSet2()
    random_set1.insert(1)
    random_set2.insert(1)
    random_set1.insert(2)
    random_set2.insert(2)
    random_set1.insert(3)
    random_set2.insert(3)
    print(random_set1)
    print(random_set1.get_random())
    random_set1.remove(3)
    print(random_set2)
    print(random_set2.get_random())
