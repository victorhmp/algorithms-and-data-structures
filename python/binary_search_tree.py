# Binary-Search-Tree property that always holds:
# Let `x` be a node in a binary search tree. If `y` is a node in the left
# subtree of `x`, then `y.key <= x.key`. If `y` is a node in the right subtree
# of `x`, then `y.key >= x.key`.

# A big advantage of binary search trees it that you can make them support
# min, max, successor, and predecessor queries in O(h) time, where h is the
# height of the tree. If the tree is balanced, then h = log(n), where n is the
# number of nodes in the tree.


class Node:
    def __init__(self, key, data) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.data = data


# Important to note that this is a simple and "purest" binary search tree, so
# the shape of the tree at any given moment will directly depend on the order
# in which elements are inserted into it. There's no self-balancing logic here,
# meaning that we might end-up with perfectly balanced trees or completely one
# sided ones. It also assumes that each key is unique.
class BinarySearchTree:
    def __init__(self, nodes) -> None:
        self.nodes = [nodes]
        self.root = nodes[0]

        for node in nodes[1:]:
            self.insert(node)

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

    # The binary search tree property is what makes it so simple to get
    # the min and max values and guarantee that they are correct.
    def min(self, subtree_root):
        while subtree_root.left != None:
            subtree_root = subtree_root.left

        return subtree_root

    def max(self, subtree_root):
        while subtree_root.right != None:
            subtree_root = subtree_root.right

        return subtree_root

    # An interesting thing to note is that we don't need to do < or > comparisons
    # to find the predecessor or successor of a node. We can just leverage the
    # binary search tree property.
    def successor(self, subtree_root):
        if subtree_root.right != None:
            return self.min(subtree_root.right)

        # If there's no subtree in the right, find the first ancestor whose left
        # child is also an ancestor of the subtree root.
        y = subtree_root.parent
        while y != None and subtree_root == y.right:
            subtree_root = y
            y = y.parent

        return y

    def insert(self, new_node):
        curr_node = self.root
        prev_node = None

        while curr_node != None:
            prev_node = curr_node
            if new_node.key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        new_node.parent = prev_node

        if prev_node == None:
            # The tree was empty
            self.root = new_node
        elif new_node.key < prev_node.key:
            prev_node.left = new_node
        else:
            prev_node.right = new_node

    # Replaces the subtree rooted at node `u` with the subtree rooted at node
    # `v`. Note that `v` can be None.
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v != None:
            v.parent = u.parent

    def delete(self, key):
        node_to_delete = self.search(self.root, key)
        if node_to_delete.left == None:
            self.transplant(node_to_delete, node_to_delete.right)
            return

        elif node_to_delete.right == None:
            self.transplant(node_to_delete, node_to_delete.left)
            return

        y = self.min(node_to_delete.right)

        if y != node_to_delete.right:
            self.transplant(y, y.right)
            y.right = node_to_delete.right
            y.right.parent = y

        self.transplant(node_to_delete, y)
        y.left = node_to_delete.left
        y.left.parent = y

    # This will print the tree in-order
    def __str__(self) -> str:
        print_buffer = []
        self.inorder_tree_walk(self.root, print_buffer)

        return str(print_buffer)


if __name__ == "__main__":
    nodes = [
        Node(15, "A"),
        Node(6, "B"),
        Node(18, "C"),
        Node(3, "D"),
        Node(7, "E"),
        Node(17, "F"),
        Node(20, "G"),
        Node(2, "H"),
        Node(4, "I"),
        Node(13, "J"),
        Node(9, "K"),
    ]

    tree = BinarySearchTree(nodes)

    print(tree)

    tree.delete(7)
    tree.delete(4)
    tree.delete(13)

    print(tree)
