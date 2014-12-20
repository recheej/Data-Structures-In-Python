__author__ = 'recheejozil'

from linked_list import LinkedList
from queue import Queue
from stack import Stack


class Graph(object):

    def __init__(self, is_weighted, num_vertices=None, head=None):

        self.adj = []

        self.weighted = is_weighted

        if head is not None:

            self.head = head
        else:
            self.head = None

        if num_vertices is not None:

            for vertex in range(0, num_vertices):

                self.adj.append(LinkedList())

    def add_edge(self, source, dest):

        self.adj[source].insert(dest)

        if not self.weighted:
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

    def dfs(self):

        stack = Stack(self.head)

        visited = []

        for vertex in range(0, len(self.adj)):
            visited.append(False)

        while not stack.is_empty():

            vertex = stack.top()

            stack.pop()

            if not visited[vertex]:

                print vertex

                visited[vertex] = True

                node = self.adj[vertex].head

                while node is not None:

                    if not visited[node.data]:

                        stack.push(node.data)

                    node = node.next