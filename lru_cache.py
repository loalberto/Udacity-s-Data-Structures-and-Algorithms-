from collections import OrderedDict


class LRU_Cache:
    def __init__(self, cap):
        self.capacity = cap
        if self.capacity == 0:
            print('The capacity is 0. No operations can be performed.')
            return
        self.capacity = cap
        self.table = OrderedDict()
        self.size = 0

    def set(self, key, value):

        if key is None or value is None:
            print('Cannot store None values')
            return

        if self.capacity == 0:
            return
        index = self.hash_code(key)
        if index in self.table:
            self.table.pop(index)
            self.table[index] = value
            return
        if self.size == self.capacity:
            lru_element = None
            for k in self.table:
                if lru_element is None:
                    lru_element = k
                    continue
                break
            self.table.pop(lru_element)
            self.table[index] = value
            return
        self.table[index] = value
        self.size += 1

    def hash_code(self, key):
        return int((31 * ord(str(key)) / 2))

    def get(self, key):

        if key is None:
            return

        if self.capacity == 0:
            return
        index = self.hash_code(key)
        if self.size == 0:
            return -1
        if index not in self.table:
            return -1
        temp = self.table[index]
        self.table.pop(index)
        self.table[index] = temp
        return temp


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(2, 2)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))       # return -1

our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry\

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# should print some warning message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should return -1

our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# should return 10
print(our_cache.get(2))
# should return 2

# A very large number will still work
our_cache.set(1, 1231231223234234543657880793)
print(our_cache.get(1))

# None values will be handled by the set function
our_cache.set(None, None)

# Trying to get a None value will be handled by the get function
print(our_cache.get(None))
