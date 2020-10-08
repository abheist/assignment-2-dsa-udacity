import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temporary = self.last
            self.last = Block(timestamp, data, temporary)
            self.last.previous_hash = temporary


def get_greenwich_time():
    utc = datetime.datetime.utcnow()
    return utc.strftime("%d/%m/%Y %H:%M:%S")


block_0 = Block(get_greenwich_time(), "Information 1", 0)
block_1 = Block(get_greenwich_time(), "Information 2", block_0)
block_2 = Block(get_greenwich_time(), "Information 3", block_1)

print(block_0.data)
print(block_0.hash)
print(block_0.timestamp)
print(block_1.previous_hash.data)

temp = LinkedList()
temp.append(get_greenwich_time(), "Information 4")
temp.append(get_greenwich_time(), "Information 5")

print(temp.last.data)
print(temp.last.previous_hash.data)
