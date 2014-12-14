__author__ = 'recheejozil'

from linked_list import Node, LinkedList


class HashData(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):

    def __init__(self, size):

        self.list = []

        for i in range(0, size):

            self.list.append(LinkedList())

    def hash_data(self, data):

        total_char_value = 0

        for char in data:

            total_char_value += ord(char)

        return total_char_value % len(self.list)

    def insert(self, key, value):

        index = self.hash_data(key)

        hash_data = HashData(key, value)

        self.list[index].insert_front(hash_data)

    def get(self, key):

        index = self.hash_data(key)

        linked_list = self.list[index]

        temp = linked_list.head

        while temp is not None:

            if temp.data.key == key:
                return temp.data.value

            temp = temp.next

        return None

    def is_empty(self):

        for chain in self.list:

            if chain.head.data is not None or chain.head.next is not None:
                return False

        return True

    def clear(self):

        for chain in self.list:

            chain.head.next = None
            chain.head.data = None

    def __str__(self):

        return str(self.list)