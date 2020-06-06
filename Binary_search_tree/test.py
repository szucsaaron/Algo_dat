class TreeNode:

    def __init__(self, data, element):

        self.left = None
        self.right = None
        self.data = data
        self.element = element

    def insert(self, data, element):
        # Comparing the value with parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data, element)
                else:
                    self.left.insert(data, element)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data, element)
                else:
                    self.right.insert(data, element)
        else:
            self.data = data

    def find(self, value):
        if value < self.data:
            if self.left is None:
                return str(value) + " not found"
            return self.left.find(value)
        elif value > self.data:
            if self.right is None:
                return str(value) + " not found"
            return self.right.find(value)
        else:
            print(str(self.data) + ' is found at node:', self.element)

    def in_order_travel(self, root):
        result = []
        if root:
            result = self.in_order_travel(root.left)
            result.append(root.data)
            result += self.in_order_travel(root.right)
        return result

    def pre_order_travel(self, root):
        result = []
        if root:
            result.append(root.data)
            result += self.pre_order_travel(root.left)
            result += self.pre_order_travel(root.right)
        return result

    def post_order_travel(self, root):
        result = []
        if root:
            result = self.post_order_travel(root.left)
            result += self.pre_order_travel(root.right)
            result.append(root.data)
        return result

    # def is_external(self, root, value):

    def min_value_node(self, node):
        current = node

        while(current.left is not None):
            current = current.left

        return current

    def delete_node(self, root, key):

        if root is None:
            return root

        if key < root.data:
            root.left = self.delete_node(root.left, key)

        elif key > root.data:
            root.right = self.delete_node(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)

            root.data = temp.data

            root.right = self.delete_node(root.right, temp.data)

            root.left = self.delete_node(root.left, temp.data)

        return root



tree = TreeNode(12, "a")
tree.insert(6, "b")
tree.insert(14, "c")
tree.insert(3, "d")
tree.insert(4, "e")
tree.insert(13, "f")
tree.insert(15, "h")

print(tree.in_order_travel(tree))
print(tree.pre_order_travel(tree))
print(tree.post_order_travel(tree))
tree.delete_node(tree, 14)
print(tree.in_order_travel(tree))