__author__ = 'recheejozil'

from linked_list import LinkedList
from queue import Queue
from stack import Stack


class Graph(object):

    def __init__(self, is_directed, num_vertices=None, head=None):

        self.adj = []

        self.visited = []

        self.directed = is_directed

        if head is not None:

            self.head = head

        else:
            self.head = None

        if num_vertices is not None:

            for vertex in range(0, num_vertices):

                self.adj.append(LinkedList())

                self.visited.append(False)

    def add_edge(self, source, dest):

        self.adj[source].insert(dest)

        if not self.directed:
            self.adj[dest].insert(source)

    def bfs(self):

        queue = Queue()

        visited = []

        queue.enqueue(self.head)
        visited.append(self.head)

        while not queue.is_empty():

            vertex = queue.front().data
            queue.dequeue()

            print vertex

            node = self.adj[vertex].head

            while node is not None:

                adj_vertex = node.data

                if adj_vertex not in visited:

                    visited.append(adj_vertex)

                    queue.enqueue(adj_vertex)

                node = node.next

    def all_visited(self):

        for vertex in self.visited:

            if not vertex:
                return False

        return True

    def dfs_recursive(self, vertex):

        if self.all_visited():
            return

        print vertex
        self.visited[vertex] = True

        adj_vertex = self.adj[vertex].head

        while adj_vertex is not None:

            if not self.visited[adj_vertex.data]:

                self.dfs_recursive(adj_vertex.data)

            adj_vertex = adj_vertex.next

    def dfs(self):

        stack = Stack()

        stack.push(self.head)

        while not stack.is_empty():

            top = stack.top()
            stack.pop()

            if not self.visited[top]:

                print top

                self.visited[top] = True

                adj_list = self.adj[top]
                adj_list = LinkedList.reverse(adj_list)

                adj_node = adj_list.head

                while adj_node is not None:

                    stack.push(adj_node.data)

                    adj_node = adj_node.next