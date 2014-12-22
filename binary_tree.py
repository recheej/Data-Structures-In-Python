__author__ = 'recheejozil'

from stack import Stack

class TreeNode(object):

    def __init__(self, item=None):

        self.key = item
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree(object):

    def __init__(self):

        self.root = None

        self.traverse_stack = Stack()

    def insert_list(self, list):

        for item in list:

            self.insert(item)

    def insert(self, item, root=None):

        if root is None:
            root = self.root

            if root is None:
                self.root = TreeNode(item)
                return

        if item < root.key:

            if root.left is None:
                root.left = TreeNode(item)
                root.left.parent = root
                return

            self.insert(item, root.left)

        if item > root.key:

            if root.right is None:
                root.right = TreeNode(item)
                root.right.parent = root
                return

            self.insert(item, root.right)

    def traverse_inorder(self, root):

        if root is None:
            return

        self.traverse_inorder(root.left)

        print root.key

        self.traverse_inorder(root.right)

    def k_largest(self, k):

        self.traverse_inorder(self.root)

        num_pops = 0

        top = self.traverse_stack.top()

        if k == 1:
            return top

        self.traverse_stack.pop()

        num_pops += 1

        while num_pops != k:

            top = self.traverse_stack.top()

            self.traverse_stack.pop()

            num_pops += 1

        return top

    def traverse_preorder(self, root):

        if root is None:
            return

        print root.key

        self.traverse_preorder(root.left)

        self.traverse_preorder(root.right)

    def traverse_postorder(self, root):

        if root is None:
            return

        self.traverse_postorder(root.left)

        self.traverse_postorder(root.right)

        print root.key

    def find(self, item):

        root = self.root

        if root.key == item:
            return root

        while root is not None:

            if root.key == item:
                return root

            if item < root.key:
                root = root.left
                continue

            if item > root.key:
                root = root.right

        return None

    def minimum(self, root):

        while root.left is not None:

            root = root.left

        return root.key

    def maximum(self, root):

        while root.right is not None:

            root = root.right

        return root.key

    def delete(self, item):

        node = self.find(item)

        if node.left is None and node.right is None:
            node = None
            return

        if node.left is None and node.right is not None:

            node = node.right
            return

        if node.left is not None and node.right is None:

            node = node.left
            return

        # TODO implement way to delete node with two children

        largest_left = self.find(self.maximum(node.left))

        self.delete(largest_left.key)

        node.key = largest_left.key

    def height(self, root):

        if root is None:
            return -1

        left_height = self.height(root.left)

        right_height = self.height(root.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def is_balanced(self, root):

        left_height = self.height(root.left)
        right_height = self.height(root.right)
        height_difference = right_height - left_height

        if height_difference < 0:
            height_difference *= -1

        return height_difference <= 1

    def sucessor(self, node):

        if node.parent == self.root and node.right is None:
            print "does not have successor"
            return

        if node.right is not None:

            print self.find(self.minimum(node.right)).key
            return

        temp_node = node

        while temp_node != temp_node.parent.left:

            temp_node = temp_node.parent

        print temp_node.parent.key