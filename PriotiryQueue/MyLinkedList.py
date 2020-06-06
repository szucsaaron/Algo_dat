from MyListNode import MyListNode


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.head = self.tail
        self.size = 0

    def get_head(self):
        """for testing purposes, returns the head of the linked list
        """
        return self.head

    def get_size(self):
        """returns the number of nodes in the linked list in O(1)
        """
        return self.size

    def add_first(self, element):
        """creates a node including the given element and adds it to the beginning of the linked list
        @param element of the new node to be added
        @raises ValueError if the element is None
        """
        if element is None:
            raise ValueError
        else:
            new_node = MyListNode(element)
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def add_last(self, element):
        """creates a node including the given element and addsit to the end of the linked list
        @param element of the new node to be added
        @raises ValueError if the element is None
        """
        if element is None:
            raise ValueError
        else:
            new_node = MyListNode(element)
            if self.head is None:
                self.head = new_node
                self.size += 1
            else:
                cur = self.head
                while cur.next:
                    cur = cur.next
                cur.next = new_node
                self.size += 1

    def add_sorted(self, element):
        """creates a node including the given element and adds it at the correct position to the linked list sorted in ascending order
        @param element of the new node to be added
        @raises ValueError if the element is None
        """
        if element is None:
            raise ValueError
        else:
            new_node = MyListNode(element)
            if self.head is None:
                new_node.next = self.head
                self.head = new_node
                self.size += 1
            elif self.head.element >= new_node.element:
                new_node.next = self.head
                self.head = new_node
                self.size += 1
            else:
                cur = self.head
                while cur.next and cur.next.element < new_node.element:
                    cur = cur.next

                new_node.next = cur.next
                cur.next = new_node
                self.size += 1

    def clear(self):
        """removes all nodes from the linked list in O(1)
        """
        self.head = None
        self.size = 0

    def remove_first(self):
        """returns the first element of the linked list and removes the node containing this element
        @return the element of the node that has been removed
        """
        if self.head is not None:
            if self.head is self.tail:
                self.tail = None
            self.head = self.head.next
            self.size -= 1

    def get_first(self):
        """returns the first element of the linked list (without removing it)
        @return element of the first node
        """
        return self.head.element

    def contains(self, element):
        """returns true if a given element is in the linked list; false otherwise
        @return True or False
        @raises ValueError if the element is None
        """
        if element is None:
            raise ValueError
        else:
            cur = self.head
            while cur is not None:
                if cur.element is element:
                    return True
                cur = cur.next
            return False

    def to_list(self):
        """returns a list representation of the linked list starting with the first element (index 0)
        @return a list
        """
        cur = self.head
        the_list = []
        while cur is not None:
            the_list.append(cur.element)
            cur = cur.next
        return the_list

    def to_string(self):
        """returns a string representation of the linked list: "[1]-> [5]-> [8]-> [20]"
        @return a string: "[1][5][8][20]"
        """
        cur = self.head
        the_string = ""
        while cur is not None:
            the_string += "["+str(cur.element)+"]"
            cur = cur.next
        return the_string

    # Support funtions

    def print_list(self):
        cur = self.head
        while cur is not None:
            print(cur.element)
            cur = cur.next

# test_list = MyLinkedList()
# test_list.add_sorted(1)
# test_list.add_sorted(9)
# test_list.add_sorted(8)
# test_list.add_sorted(2)
# test_list.add_sorted(11)
# test_list.print_list()
# print("With remove first")
# test_list.remove_first()
# test_list.print_list()
# print(test_list.contains(5))
# my_list = test_list.to_list()
# print(my_list)
# my_string = test_list.to_string()
# print(my_string)
# print(test_list.get_first())
# test_list.clear()
# print("My list after clear func")
# test_list.print_list()
# test_list.add_sorted(1)
# test_list.add_sorted(9)
# test_list.print_list()
