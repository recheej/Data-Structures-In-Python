__author__ = 'recheejozil'

from linked_list import LinkedList
from hash_table import HashTable
import strings
from stack import Stack
from queue import Queue, MyQueue
from binary_tree import BinarySearchTree
from graph import Graph


def main():

    tree = BinarySearchTree()

    tree.insert_list([1, 2, 3, 4, 5])

    print tree.k_largest(3)


main()