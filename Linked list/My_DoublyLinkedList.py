from My_ListNode import My_ListNode


def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


class My_DoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    """/***********************************************************
	* DON'T TOUCH THIS CODE
	* Methods for testing your code after submission.
	***********************************************************/"""

    _myList_head = None
    _myList_tail = None
    _myList_size = 0

    def __init__(self, new_head=None, new_tail=None, new_size=0):
        """Create a list and default values are None."""
        self._header = new_head
        self._tail = new_tail
        self._size = new_size

    def _len_(self):
        """Return the number of elements in the list."""
        return self._size

    def list_is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _get_header(self):
        return self._header

    def _get_tail(self):
        return self._tail

    """/***********************************************************
	***********************************************************/"""

    def insert_ordered(self, integer_val):
        try:
            int(integer_val)
        except ValueError:
            print("ValueError: Give and integer!")
            return

        p = My_ListNode(integer_val)

        if self._header is None:
            self._header = p
            self._tail = p
            self._header.prev_val = None
            self._size += 1
            return

        if p.data < self._header.data:
            p.prev_val = None
            self._header.prev_val = p
            p.next_val = self._header
            self._header = p
            self._size += 1
            return

        if p.data > self._tail.data:
            p.prev_val = self._tail
            self._tail.next_val = p
            self._tail = p
            self._size += 1
            return

        temp = self._header.next_val
        while temp.data < p.data:
            temp = temp.next_val

        temp.prev_val.next_val = p
        p.prev_val = temp.prev_val
        temp.prev_val = p
        p.next_val = temp
        self._size += 1

    def delete_element_by_value(self, integer_val):
        try:
            int(integer_val)
        except ValueError:
            print("ValueError: Give and integer!")
            return False

        current = self._header
        while current:
            if current.data == integer_val and current == self._header:
                # Case 1:
                if not current.next_val:
                    current = None
                    self._header = None
                    return

                # Case 2:
                else:
                    nxt = current.next_val
                    current.next_val = None
                    nxt.prev_val = None
                    current = None
                    self._header = nxt
                    return

            elif current.data == integer_val:
                # Case 3:
                if current.next_val:
                    nxt = current.next_val
                    prev = current.prev_val
                    prev.next_val = nxt
                    nxt.prev_val = prev
                    current.next_val = None
                    current.prev_val = None
                    current = None
                    return

                # Case 4:
                else:
                    prev = current.prev_val
                    prev.next_val = None
                    current.prev_val = None
                    current = None
                    return
            current = current.next_val

    def delete_node(self, delete):

        if self._header is None or delete is None:
            return None

        if self._header == delete:
            self._header = delete.next_val

        if delete.next_val is not None:
            delete.next_val.prev_val = delete.prev_val

        if delete.prev_val is not None:
            delete.prev_val.next_val = delete.next_val

        delete = None
        return self._header

    def _remove_(self, integer_val):
        # if list is empty
        if self._header is None:
            return False

        current = self._header

        # traverse the list up to the end
        while current is not None:

            if current.data == integer_val:

                next = current.next_val

                self._header = self.delete_node(current)

                current = next

            else:
                current = current.next_val
        return True

    def remove_duplicates(self):
        cur = self._header
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next_val
            else:
                nxt = cur.next_val
                self.delete_node(cur)
                cur = nxt

    def reorder_list(self):
        if self._header is None:
            return
        else:
            n = self._header
            even = []
            odd = []
            while n is not None:

                if n.data % 2 == 1:
                    odd.append(n.data)
                else:
                    even.append(n.data)
                n = n.next_val
            bubble_sort(even)
            bubble_sort(odd)

            # Deleting everything from the doubly linked list
            for i in range(len(even)):
                self.delete_element_by_value(even[i])
                self._size -= 1
            for i in range(len(odd)):
                self.delete_element_by_value(odd[i])
                self._size -= 1

            # Inserting everything back in order to the doubly linked list

            for i in range(len(odd)):
                if i == 0:
                    self.insert_in_empty_list(odd[i])
                    self._size += 1
                else:
                    self.insert_at_end(odd[i])
                    self._size += 1
            index = i + 1
            if len(even) == 0:
                index = -1
            else:
                for i in range(len(even)):
                    self.insert_at_end(even[i])
                    self._size += 1
            return index

    def get_integer_value(self, index):
        try:
            if index + 1 > self._size:
                raise ValueError
        except ValueError:
            print("ValueError: Index out of range!")
            return
        if self._header is None:
            print("List has no element")
            return
        else:
            n = self._header
            i = 0
            found = False
            while n is not None:
                if i == index:
                    return n.data
                n = n.next_val
                i += 1

    def insert_in_empty_list(self, data):
        if self._header is None:
            new_node = My_ListNode(data)
            self._header = new_node
        else:
            print("list is not empty")
            return

    def traverse_list(self):
        if self._header is None:
            print("List has no element")
            return
        else:
            n = self._header
            while n is not None:
                print(n.data)
                n = n.next_val

    def iter(self):
        if self._header is None:
            print("List has no element")
            return
        else:
            n = self._header
            while n is not None:
                yield n.data
                n = n.next_val

    def insert_at_end(self, data):
        if self._header is None:
            new_node = My_ListNode(data)
            self._header = new_node
            return
        n = self._header
        while n.next_val is not None:
            n = n.next_val
        new_node = My_ListNode(data)
        n.next_val = new_node
        new_node.prev_val = n