# Binary-Search-Tree property that always holds:
# Let `x` be a node in a binary search tree. If `y` is a node in the left
# subtree of `x`, then `y.key <= x.key`. If `y` is a node in the right subtree
# of `x`, then `y.key >= x.key`.

class Node:
    def __init__(self, key, data) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self, nodes) -> None:
        self.root = None
        self.nodes = [nodes]

    # This tree walk will take O(n) time for the whole tree.
    def inorder_tree_walk(self, x, print_buffer):
        if x != None:
            self.inorder_tree_walk(x.left, print_buffer)
            print_buffer.append(x.key)
            self.inorder_tree_walk(x.right, print_buffer)

    def search_recursive(self, x, key):
        if x == None or key == x.key:
            return x
        
        if key < x.key:
            return self.search_recursive(x.left, key)

        return self.search_recursive(x.right, key)

    # This is an iterative version of the search that will actually be more
    # efficient in real world applications.
    def search(self, x, key):
        while x != None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right

        return x

    # This will print the tree in-order
    def __str__(self) -> str:
        print_buffer = []
        self.inorder_tree_walk(self.root, print_buffer)

        return str(print_buffer)
