from hash_table import HashTable

if __name__ == "__main__":
    table = HashTable()

    table.insert(0, "value1")
    table.insert(1, "value2")
    table.insert(2, "value3")
    print(table.get_hashmap())

    print(table.get(0))
    print(table.delete(2))

    print(table.get_hashmap())
