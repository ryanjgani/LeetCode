class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        key = node.key
        prevNode, nextNode = node.prev, node.next
        prevNode.next , nextNode.prev = nextNode, prevNode
        return key
    
    def insert(self, node):
        MRU = self.right.prev
        MRU.next = self.right.prev = node
        node.prev, node.next = MRU, self.right 
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else: return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
            if len(self.cache.keys()) > self.capacity:
                pop = self.remove(self.left.next)
                self.cache.pop(pop)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)