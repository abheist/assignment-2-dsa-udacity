import hashlib
import datetime
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data, timestamp)

    def calc_hash(self, data, timestamp):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        sha.update(timestamp.encode('utf-8'))
        return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, data):
        if not self.head:
            self.head = Block(get_greenwich_time(), data, 0)
            self.last = self.head
        else:
            temporary = self.last
            self.last = Block(get_greenwich_time(), data, temporary)
            self.last.previous_hash = temporary


def get_greenwich_time():
    utc = datetime.datetime.utcnow()
    return utc.strftime("%d/%m/%Y %H:%M:%S")


temp = LinkedList()
temp.append("To the well-organized mind, death is but the next great adventure!")
temp.append("Dobby is free.")
print(temp.last.data)
print(temp.last.previous_hash.data)


temp1 = LinkedList()
temp1.append("")
temp1.append("Dobby is free.")
print(temp1.last.data)
print(temp1.last.previous_hash.data)


temp2 = LinkedList()
temp2.append("")
temp2.append("")
print(temp2.last.data)
print(temp2.last.previous_hash.data)
