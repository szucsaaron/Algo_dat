"""
Author: Aron Abraham Szucs
Matr.Nr.: 11932493
Assigment 5
"""

import datetime
from TreeNode import TreeNode
import random


class MyBinarySearchTree:
    def __init__(self, root=None):
        self._root = root
        self._size = 0

    def insert(self, new_node):
        """@params new_node to insert.
        @return success if the insert operation was successful.
        @raises ValueError if Node is None.
        Insert the element elem into the tree and return True if it was successful.
        Elements with the same key are not allowed, in this case False is returned.
        None-elements are not allowed, in this case an exception is thrown.
        """
        if new_node is None:
            raise ValueError("Node to be inserted must not be None")
        if self.find(new_node.key):
            print(self.find(new_node.key))
            return False
        if self._root is None:
            self._root = new_node
        else:
            self._insert_helper(self._root, new_node)
        self._size += 1
        return True

    def get_parent(self, key):
        """@param key
        @return key of parent.
        @raises ValueError if key is None.
        Search the parent node of a given key and return its key or None if not found.
        """
        if key is None:
            raise ValueError("Key must be different than None")
        return self.parent_helper(self._root, key).parent.key

    def is_root(self, key):
        """@params key
        @return boolean
        @raises ValueError if key is None.
        Returns True if the node of any given key is the root node, else returns False.
        """
        if key is None:
            raise ValueError
        if key is self._root.key:
            return True
        else:
            return False

    def get_size(self):
        """@return Tree size.
        returns the number of items in the tree.
        """
        return self._size

    def find(self, key):
        """@params key
        @return The corresponding element of the node with the given key.
        @raises ValueError if key is None
        Returns the element of the node found with the given key, or None if element was not found.
        """
        if self._root:
            return self.find_helper(self._root, key)
        else:
            return None

    def remove(self, key):
        """@params key
        @return success of the remove operation.
        @raises ValueError if key is None.
        Removes the element with the given key, and returns True if element was found AND removed, else False.
        """
        if key is None:
            raise ValueError
        if self.find(key) is None:
            return False
        self._root = self.delete_helper(self._root, key)
        self._size -= 1
        return True

    def is_external(self, key):
        """@params key
        @return boolean
        @raises ValueError if key is None.
        Return True if the node with the given key is an external node, otherwise return False.
        """
        if key is None:
            raise ValueError
        if self._root:
            if self.is_external_helper(self._root, key).right_node is None and self.is_external_helper(self._root,
                                                                                                       key).left_node is None:
                return True
            else:
                return False

    def is_internal(self, key):
        """@params key
        @return boolean
        @raises ValueError if key is None.
        Return True if the node with the given key is an internal node, otherwise return False.
        """
        if key is None:
            raise ValueError
        if not self.is_external(key):
            return True
        else:
            return False

    def to_array_inorder(self, cur, print_array):
        """@return array
        Returns an array-representation of the stored elements (Inorder traversal).
        """
        if cur:
            print_array = self.to_array_inorder(cur.left_node, print_array)
            print_array.append(cur.key)
            print_array = self.to_array_inorder(cur.right_node, print_array)
        return print_array

    def to_array_preorder(self, cur, print_array):
        """@return array
        Returns an array-representation of the stored elements (Preorder traversal).
        """
        if cur:
            print_array.append(cur.key)
            print_array = self.to_array_preorder(cur.left_node, print_array)
            print_array = self.to_array_preorder(cur.right_node, print_array)
        return print_array

    def to_array_postorder(self, cur, print_array):
        """@return array
        Returns an array-representation of the stored elements (Postorder traversal).
        """
        if cur:
            print_array = self.to_array_postorder(cur.left_node, print_array)
            print_array = self.to_array_postorder(cur.right_node, print_array)
            print_array.append(cur.key)
        return print_array

    def is_bst(self, tree):
        """@params tree is an instance of binary search tree.
        @return True if the given tree is a binary search tree, else False.
        @raises ValueError if the tree is empty or None.
        This method verifies a given BianryTree, if it is a correct Binary Search Tree.
        """
        if tree is None:
            raise ValueError
        if tree.get_size() is 0:
            return False
        test_array = []
        tree.to_array_inorder(tree._root, test_array)
        if test_array == sorted(test_array):
            return True
        else:
            return False

    def return_min_key(self):
        """@return element of the minium key.
        Searches and returns the element of the smallest key in the bst.
        """
        cur = self._root
        if cur.left_node is None:
            return cur.key
        else:
            while cur.left_node is not None:
                cur = cur.left_node
        return cur.key

    def runtime_comparison(self, linear_list, key):
        """Creates a binary search tree abased on the given (linear) list and then determines runtime and number
        of comparisons needed to search a key in both, the internal BST and in the list. The time needed for the
        search in list and BST shall be printed on the terminal, the number of comparisons needed shall be returned
        in an array (index 0 = BST, index 1 = list)
        @param list
        @param key The key to be search in list and BST.
        @return The number of comparisons needed to find the given key in the BST.
        @raises ValueError if one of the parameters is None.
        """
        if linear_list is None or key is None:
            raise ValueError

        start1 = datetime.datetime.now()
        # comparisons1 = 0
        comparisons1 = self.find2(key, 0)[1]
        # print(asd)
        # print("asd", asd[1])
        stop1 = datetime.datetime.now()
        delta1 = stop1 - start1
        difference1 = delta1.total_seconds()

        print("Time required for BST:", difference1)

        start2 = datetime.datetime.now()
        comparisons2 = bubble_search(linear_list, key)
        stop2 = datetime.datetime.now()
        delta2 = stop2 - start2
        difference2 = delta2.total_seconds()

        print("Time required for linear list:", difference2)

        return comparisons1, comparisons2

    def get_depth(self, node):
        """@param node The node of which the depth should be determined.
        @return The depth of the node.
        Determines the depth of a node in the tree.
        """
        if self.is_root(node.key):
            return 0
        return self.get_depth(node.parent) + 1

    def is_tree_complete(self):
        """Analyses the tree and determines if it is complete.
        @return True if the tree is complete, False otherwise.
        """
        cur = self._root
        while cur.left_node is not None:
            cur = cur.left_node
        depth = self.get_depth(cur)
        if self._size == (pow(2, depth + 1) - 1):
            return True
        else:
            return False

    ''''''''''''''''''
    '''Support Functions'''
    ''''''''''''''''''

    def _insert_helper(self, cur, new_node):
        if cur.key < new_node.key:
            if cur.right_node is None:
                cur.right_node = new_node
                new_node.parent = cur
            else:
                self._insert_helper(cur.right_node, new_node)
        else:
            if cur.left_node is None:
                cur.left_node = new_node
                new_node.parent = cur
            else:
                self._insert_helper(cur.left_node, new_node)

    def return_min_node_from_node(self, node):
        cur = node

        while cur.left_node is not None:
            cur = cur.left_node

        return cur

    def delete_helper(self, cur, key):
        if cur is None:
            return None

        if key < cur.key:
            cur.left_node = self.delete_helper(cur.left_node, key)

        elif key > cur.key:
            cur.right_node = self.delete_helper(cur.right_node, key)

        else:

            if cur.left_node is None:
                temp = cur.right_node
                cur = None
                return temp

            elif cur.right_node is None:
                temp = cur.left_node
                cur = None
                return temp

            temp = self.return_min_node_from_node(cur.right_node)
            cur.key = temp.key
            cur.right_node = self.delete_helper(cur.right_node, temp.key)

        return cur

    def find_helper(self, cur, key):
        if key > cur.key:
            if cur.right_node:
                return self.find_helper(cur.right_node, key)
            else:
                return None
        elif key < cur.key:
            if cur.left_node:
                return self.find_helper(cur.left_node, key)
            else:
                return None
        elif key is cur.key:
            return cur.element

    def find2(self, key, comparisons):
        """@params key
        @return The corresponding element of the node with the given key.
        @raises ValueError if key is None
        Returns the element of the node found with the given key, or None if element was not found.
        """
        if self._root:
            return self.find2_helper(self._root, key, comparisons)
        else:
            return None

    def find2_helper(self, cur, key, comparisons):
        comparisons += 3
        if key > cur.key:
            if cur.right_node:
                return self.find2_helper(cur.right_node, key, comparisons)
            else:
                return None
        elif key < cur.key:
            if cur.left_node:
                return self.find2_helper(cur.left_node, key, comparisons)
            else:
                return None
        elif key is cur.key:
            return (cur.element, comparisons)

    def parent_helper(self, cur, key):
        if key > cur.key:
            if cur.right_node:
                return self.parent_helper(cur.right_node, key)
            else:
                return None
        elif key < cur.key:
            if cur.left_node:
                return self.parent_helper(cur.left_node, key)
            else:
                return None
        elif key is cur.key:
            return cur

    def is_external_helper(self, cur, key):
        if key > cur.key:
            if cur.right_node:
                return self.is_external_helper(cur.right_node, key)
            else:
                return None
        elif key < cur.key:
            if cur.left_node:
                return self.is_external_helper(cur.left_node, key)
            else:
                return None
        elif key is cur.key:
            return cur


''''''''''''''''''
'''Test Code'''
''''''''''''''''''

test_bst = MyBinarySearchTree()
test_bst.insert(TreeNode(key=5, element="a"))
test_bst.insert(TreeNode(key=3, element="b"))
test_bst.insert(TreeNode(key=7, element="c"))
test_bst.insert(TreeNode(key=2, element="d"))
test_bst.insert(TreeNode(key=4, element="e"))
test_bst.insert(TreeNode(key=6, element="f"))
test_bst.insert(TreeNode(key=9, element="g"))
x = TreeNode(key=8, element="h")
test_bst.insert(x)

print("inorder:", test_bst.to_array_inorder(test_bst._root, []))
print("preorder:", test_bst.to_array_preorder(test_bst._root, []))
print("postorder:", test_bst.to_array_postorder(test_bst._root, []))
print("find 5:", test_bst.find(5))
test_bst.remove(9)
print("preorder after removing 9:", test_bst.to_array_preorder(test_bst._root, []))
print("is 1 root:", test_bst.is_root(1))
print("size:", test_bst.get_size())
print("parent of 6:", test_bst.get_parent(6))
print("is 7 external:", test_bst.is_external(7))
print("min key:", test_bst.return_min_key())
# test_bst.remove(None)
print("is bst:", test_bst.is_bst(test_bst))
print("depth of 8:", test_bst.get_depth(x))
print("complete:", test_bst.is_tree_complete())
empty_bst = MyBinarySearchTree()
print("is empty bst valid bst:", empty_bst.is_bst(empty_bst))


def bubble_search(my_list, key):
    for i in range(len(my_list)):
        if my_list[i] is key:
            return i
    return "Not found"


# Test case 1
print("\n\nRUNTIME COMPARISONS\n")
print("TEST 1\n")
random_list = [8, 17, 10, 1, 3]
comp_bst = MyBinarySearchTree()
comp_bst.insert(TreeNode(key=8, element="a"))
comp_bst.insert(TreeNode(key=17, element="b"))
comp_bst.insert(TreeNode(key=10, element="c"))
comp_bst.insert(TreeNode(key=1, element="d"))
comp_bst.insert(TreeNode(key=3, element="e"))

comps = comp_bst.runtime_comparison(random_list, 3)
print("BST:", comps[0], "Linear list:", comps[1])

print("\nTEST 2\n")
# Test case 2
random_list2 = []
comp_bst2 = MyBinarySearchTree()
for i in range(100000):
    number = random.randint(1, 1000000)
    random_list2.append(number)
    comp_bst2.insert(TreeNode(key=number, element=str(number)))

# number is going to be equal to the last inserted element, so

comps2 = comp_bst2.runtime_comparison(random_list2, number)
print("BST:", comps2[0], "Linear list:", comps2[1])
