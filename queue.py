__author__ = 'recheejozil'

from linked_list import LinkedList
from linked_list import Node
from stack import Stack


class Queue(object):

    def __init__(self):

        self.linked_list = LinkedList()

    def enqueue(self, item):

        if self.linked_list.head is None:

            self.linked_list.insert(item)

            return

        node = Node(item)

        self.linked_list.tail.next = node

        self.linked_list.tail = self.linked_list.tail.next

    def dequeue(self):

        self.linked_list.delete_node(self.linked_list.head)

    def front(self):

        return self.linked_list.head.data

    def is_empty(self):

        if self.linked_list.head is None:
            return True

        return False

    def size(self):

        return self.linked_list.size()


class MyQueue(object):

    def __init__(self):

        self.stack_one = Stack()
        self.stack_two = Stack()

    def enqueue(self, item):

        if self.stack_one.is_empty():

            self.stack_one.push(item)
            return

        while not self.stack_one.is_empty():

            temp = self.stack_one.top()

            self.stack_one.pop()

            self.stack_two.push(temp)

        self.stack_one.push(item)

        while not self.stack_two.is_empty():

            temp = self.stack_two.top()

            self.stack_two.pop()

            self.stack_one.push(temp)

    def dequeue(self):

        self.stack_one.pop()