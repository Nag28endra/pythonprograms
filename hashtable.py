class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

hash_table = HashTable(10)

hash_table.insert(5, "apple")
hash_table.insert(15, "banana")
hash_table.insert(25, "cherry")

print(hash_table.search(15))  # Output: "banana"

hash_table.remove(15)

print(hash_table.search(15))  # Output: None
