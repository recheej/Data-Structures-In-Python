__author__ = 'recheejozil'

from linked_list import LinkedList
from hash_table import HashTable
import strings
from stack import Stack
from queue import Queue, MyQueue
from binary_tree import BinarySearchTree


def main():

    tree = BinarySearchTree()

    tree.insert_list([25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90, 60])

    tree.traverse_postorder(tree.root)

    node = tree.find(0)

    print tree.minimum()

    print tree.maximum()

main()