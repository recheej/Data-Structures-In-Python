__author__ = 'recheejozil'

from linked_list import LinkedList
from linked_list import Node


class Queue(object):

    def __init__(self):

        self.linked_list = LinkedList()

    def enqueue(self, item):

        if self.linked_list.head is None:

            self.linked_list.insert(5)

            return

        tail = self.linked_list.tail

        tail.next = Node(item)

        self.linked_list.tail = tail.next

    def dequeue(self):

        self.linked_list.delete_node(self.linked_list.head)

    def front(self):

        return self.linked_list.head

    def is_empty(self):

        if self.linked_list.head is None:
            return True

        return False

    def size(self):

        return self.linked_list.size()