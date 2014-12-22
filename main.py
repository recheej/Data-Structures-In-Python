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

    tree.insert_list([20, 8, 22, 4, 12, 10, 14])

    sucessor = tree.sucessor(tree.find(20))


main()