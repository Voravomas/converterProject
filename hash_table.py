from temp.myarray import MyArray

# An example of using a hash table from 'http://blog.chapagain.com.np/
# hash-table-implementation-in-python-data-structures-algorithms/'


class HashTable:
    """
    An implementation of hash table modified to be built on ADT Array.
    """

    def __init__(self, num):
        """
        A method that initializes array of arrays.
        :param num: Sets length of table
        """
        self.num = num
        tempArr = MyArray(num)
        for i in range(num):
            tempArr[i] = MyArray(num)
        self.hash_table = tempArr

    def insert(self, key, value):
        """
        A method that allows to insert a key and value.
        """
        hash_key = hash(key) % len(self.hash_table)
        key_exists = False
        bucket = self.hash_table[hash_key]

        if not bucket.isEmpty:
            i = 0
            for keyVal in range(len(bucket)):
                myKey, myValue = bucket[keyVal]
                if key == myKey:
                    key_exists = True
                    break
                i += 1
        if key_exists:
            bucket[i] = ((key, value))
        else:
            for emptySearch in range(self.num):
                if bucket[emptySearch] is None:
                    bucket[emptySearch] = ((key, value))
                    break

    def search(self, key):
        """
        A method that allows to search value by using key.
        """
        hash_key = hash(key) % len(self.hash_table)
        bucket = self.hash_table[hash_key]
        for keyVal in range(len(bucket)):
            myKey, myValue = bucket[keyVal]
            if key == myKey:
                return myValue
