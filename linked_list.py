__author__ = 'recheejozil'


class Node(object):

    def __init__(self, data=None):

        self.data = data
        self.next = None
        self.prev = None


class LinkedList(object):

    def __init__(self):

        self.head = None
        self.tail = None

    @staticmethod
    def reverse(linked_list):

        new_list = LinkedList()

        temp = linked_list.tail

        while temp is not None:

            new_list.insert(temp.data)

            temp = temp.prev

        return new_list

    def insert(self, item):

        temp = self.head

        if temp is None:
            self.head = Node(item)
            self.tail = self.head
            return

        while temp.next is not None:

            temp = temp.next

        temp.next = Node(item)
        temp.next.prev = temp
        self.tail = temp.next

    def insert_front(self, item):

        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
            return

        new_head = Node(item)
        new_head.next = self.head
        self.head = new_head

    def search(self, item):

        temp = self.head

        while temp is not None:

            if temp.data == item:

                return temp

            temp = temp.next

        return None

    def delete(self, item):

        temp = self.head

        if temp.data == item:

            if temp.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = temp.next

            return

        while temp.next is not None:

            if temp.next.data == item:

                temp.next = temp.next.next

                return

            temp = temp.next

    def delete_duplicates(self):

        temp = self.head

        while temp is not None:

            temp_two = self.head

            prev = temp

            while temp_two is not None:

                if not temp_two is temp:

                    if temp_two.data == temp.data:

                        prev.next = temp_two.next

                prev = temp_two
                temp_two = temp_two.next

            temp = temp.next

    def n_to_last_node(self, n):

        temp_one = self.head
        temp_two = temp_one

        counter = 0

        while True:

            if counter == n - 1:
                break

            counter += 1
            temp_two = temp_two.next

        if temp_two.next is None:
            return temp_one

        while temp_two.next is not None:

            temp_one = temp_one.next
            temp_two = temp_two.next

        return temp_one

    def delete_node(self, node):

        if node == self.head and node.next is None:
            self.tail = None
            self.head = None
            return

        if node.next is None:

            node = None
            self.tail = None
            return

        next_node = node.next

        node.data = next_node.data
        node.next = next_node.next

    def start_cycle_node(self):

        temp_one = self.head
        temp_two = temp_one

        while True:

            temp_one = temp_one.next
            temp_two = temp_two.next.next

            if temp_one == temp_two:

                temp_one = self.head
                break

        while True:

            temp_one = temp_one.next
            temp_two = temp_two.next

            if temp_one == temp_two:
                return temp_one

    def size(self):

        temp = self.head

        if temp is None:
            return 0

        list_size = 0

        while temp is not None:

            list_size += 1

            temp = temp.next

        return list_size

    def __str__(self):

        temp = self.head

        rep_string = ""
        while temp is not None:

            rep_string += " " + str(temp.data)

            temp = temp.next


        return rep_string