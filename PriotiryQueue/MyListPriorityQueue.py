from MyLinkedList import MyLinkedList


class MyListPriorityQueue:
    def __init__(self):
        self.list = MyLinkedList()

    def get_size(self):
        """returns the number of elements in the PQ
        @return number of elements
        """
        return self.list.get_size()

    def is_empty(self):
        """determines if the PQ is empty or not
        @return True or False
        """
        if self.list.size is 0:
            return True
        else:
            return False

    def insert(self, element):
        """creates a node including the given element and adds it in the PQ
        @param element: the element to be added
        @raises ValueError if element is None
        """
        if element is None:
            raise ValueError
        else:
            self.list.add_sorted(element)

    def remove_min(self):
        """returns and removes the node containing the minimum element from the PQ
        @return the element from the node that has been removed or None if the element was not found
        """
        self.list.remove_first()

    def get_min(self):
        """Returns the minimum element of the PQ without removing the node containing it
        @return the minimum element of the PQ or None if the element was not found
        """
        return self.list.get_first()


    def to_list(self):
        """Returns a list representation of the PQ
        @return a list
        """
        return self.list.to_list()

    def to_string(self):
        """Returns a string representation of the PQ
        @return a string
        """
        return self.list.to_string()

# pq = MyListPriorityQueue()
# pq.insert(100)
# pq.insert(10)
# pq.insert(50)
# pq.remove_min()
# print(pq.get_size())
# print(pq.get_min())
# print(pq.to_string())
# print(pq.to_list())