
def scream():
    print('ahhhhh!')

user = {
    'age': 54,
    'name': 'Kylie',
    'magic': True,
    'scream' : scream(),

}

class HashTable:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size

    def _hash(self, key):
        hash = 0
        i = 0
        while i < len(key):
            hash = (hash + ord(key[i]) * i) % len(self.data)
            i += 1
        return hash


    def get(self, key):
        key = str(key)
        hashed_key = self._hash(key)
        data = self.data[hashed_key]
        if len(data) > 0:
            for record in data:
                if record[0].lower() == key.lower():
                    return record[1]
        return None


    def set(self, key, value):
        key = str(key)
        hashed_key = self._hash(key)
        if not self.data[hashed_key]:
            self.data[hashed_key] = []
        self.data[hashed_key].append([key, value])
        return self.data

hashTable = HashTable(100)
hashTable.set('Language', 'Python')
hashTable.set('Version', '3.0')
hashTable.set(1, 'Number')
print(hashTable.get('1'))



