class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def search(self, key):
        key_hash = self.hash_function(key)
        values = self.table[key_hash]
        for i in values:
            if i == key:
                return i
        return None


file_path = "input.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()

hash_table = HashTable(10)

for word in words:
    hash_table.insert(word)


search_key = "123"
result = hash_table.search(search_key)
print(result)
