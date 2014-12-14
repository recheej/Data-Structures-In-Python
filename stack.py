__author__ = 'recheejozil'

from linked_list import LinkedList


class Stack(object):

    def __init__(self):

        self.linked_list = LinkedList()

    def push(self, item):

        self.linked_list.insert_front(item)

    def pop(self):

        self.linked_list.delete_node(self.linked_list.head)

    def top(self):

        return self.linked_list.head.data

    def is_empty(self):

        if self.linked_list.head is None:
            return True

        return False

    def size(self):

        return self.linked_list.size()