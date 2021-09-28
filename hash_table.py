class HashTable:
    def __init__(self):
        self.size = 8
        self.hashmap = [[] for _ in range(self.size)]

    def hashing_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def insert(self, key, value):
        global i
        hash_key = self.hashing_func(key)
        key_exist = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exist = True
                break
        if key_exist:
            bucket[i] = (key, value)
            return bucket
        else:
            bucket.append((key, value))
            return bucket

    def get(self, key):
        hash_key = self.hashing_func(key)
        bucket = self.hashmap[hash_key]
        if bucket:
            for kv in bucket:
                k, v = kv
                if key == k:
                    return bucket
        elif not bucket:
            raise KeyError("does not exist")

    def delete(self, key):
        global i
        hash_key = self.hashing_func(key)
        key_exist = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exist = True
                break
        if key_exist:
            del bucket[i]
            return key
        else:
            raise KeyError("does not exist")

    def get_hashmap(self):
        return self.hashmap
