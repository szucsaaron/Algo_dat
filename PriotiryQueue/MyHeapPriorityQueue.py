class MyHeapPriorityQueue:
    def __init__(self, init_capicity):
        """@param init_capicity: the initial capacity of the min heap
        """
        self.heap = init_capicity * [None]
        self.size = 0
        self.init_capicity = init_capicity

    def get_heap(self):
        """for testing purposes only
        """
        return self.heap

    def parent(self, index):
        return int((index - 1) / 2)

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, element):
        """inserts an element in the min heap
        @param element: the element to be inserted
        @raises ValueError if element is None
        """
        if element is None:
            raise ValueError
        else:
            if self.size >= self.init_capicity:
                self.heap += self.init_capicity * [None]
                self.init_capicity *= 2

            self.heap[self.size] = element
            self.size += 1
            self.up_heap(self.size - 1)

    def up_heap(self, index):
        while self.has_parent(index) and self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def down_heap(self, index):
        while self.has_left_child(index):
            min_child_ind = self.get_min_child_index(index)
            if min_child_ind is None:
                break
            if self.heap[index] > self.heap[min_child_ind]:
                self.swap(index, min_child_ind)
                index = min_child_ind
            else:
                break

    def is_empty(self):
        """returns True if the min heap is empty, False otherwise
        @return True or False
        """
        if self.size is 0:
            return True
        else:
            return False

    def get_min(self):
        """returns the minimum element of the min heap without removing the node containing it or None if the element was not found
        @return the minimum element or None
        """
        if self.size is 0:
            return None
        else:
            return self.heap[0]

    def remove_min(self):
        """returns the minimum element of the min heap and removes the node containing it or None if the element was not found
        @return the minimum element or None
        """
        if self.size is 0:
            return None
        else:
            last_index = self.size - 1
            minimum = self.heap[0]
            self.swap(0, last_index)
            self.heap[last_index] = None
            self.down_heap(0)
            self.size -= 1
            return minimum

    def get_size(self):
        """returns the number of elements in the min heap
        @return element count
        """
        return self.size

    # ---SUPPORT FUNCTIONS--- #

    def has_parent(self, index):
        return self.parent(index) >= 0

    def has_left_child(self, index):
        return self.left_child(index) < self.size

    def has_right_child(self, index):
        return self.right_child(index) < self.size

    def get_min_child_index(self, index):
        if self.has_left_child(index):
            left_c = self.left_child(index)
            if self.has_right_child(index):
                right_c = self.right_child(index)
                if self.heap[left_c] is None:
                    return right_c
                elif self.heap[right_c] is None:
                    return left_c
                elif self.heap[left_c] < self.heap[right_c]:
                    return left_c
                else:
                    return right_c

    # --------------------- #
