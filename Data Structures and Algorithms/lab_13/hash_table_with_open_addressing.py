class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None


file_path = "input.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()


hash_table = HashTable(50)
words = text.split()

for word in words:
    hash_table.insert(word, word)


search_key = "sample"
result = hash_table.search(search_key)
print(result)
