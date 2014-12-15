__author__ = 'recheejozil'


class TreeNode(object):

    def __init__(self, item=None):

        self.key = item
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self):

        self.root = None

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
                return

            self.insert(item, root.left)

        if item > root.key:

            if root.right is None:
                root.right = TreeNode(item)
                return

            self.insert(item, root.right)

    def traverse_inorder(self, root):

        if root is None:
            return

        self.traverse_inorder(root.left)

        print root.key

        self.traverse_inorder(root.right)

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

    def minimum(self):

        root = self.root

        while root.left is not None:

            root = root.left

        return root.key

    def maximum(self):

        root = self.root

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

        node_to_replace = node.right

        # TODO implement way to delete node with two children


