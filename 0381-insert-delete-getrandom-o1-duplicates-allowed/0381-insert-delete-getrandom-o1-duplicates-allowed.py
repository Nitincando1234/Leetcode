class RandomizedCollection:

    def __init__(self):
        self.hashmap = collections.defaultdict(set)        
        self.list = []

    def insert(self, val: int) -> bool:
        self.hashmap[val].add(len(self.list))
        self.list.append(val)
        return len(self.hashmap[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.hashmap[val]: return False
        else:
            lastElement = self.list[-1]
            index = self.hashmap[val].pop()
            self.list[index] = lastElement
            self.hashmap[lastElement].add(index)
            self.hashmap[lastElement].discard(len(self.list) - 1)
            self.list.pop()
            return True
            
    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()