class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}

    def get(self, key: int) -> int:
        if key in self.storage:
            value = self.storage.pop(key)
            self.storage[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.storage.pop(key)
            
        self.storage[key] = value
        
        if len(self.storage) > self.capacity:
            self.removeOldest()

    def removeOldest(self):
        self.storage.pop(next(iter(self.storage.keys())))   