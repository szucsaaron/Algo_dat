from My_DoublyLinkedList import My_DoublyLinkedList
from My_ListNode import My_ListNode

my_test_list = None


# requires that insertSorted() and remove() works correctly
def test_len_():
    global my_test_list
    my_test_list = My_DoublyLinkedList()
    assert my_test_list._len_() == 0

    my_test_list.insert_ordered(1)
    assert my_test_list._len_() == 1

    my_test_list.insert_ordered(20)
    my_test_list.insert_ordered(13)
    assert my_test_list._len_() == 3

    my_test_list.insert_ordered(4)
    my_test_list.insert_ordered(9)
    assert my_test_list._len_() == 5

    my_test_list.insert_ordered(24)
    assert my_test_list._len_() == 6


def test_list_is_empty():
    global my_test_list
    my_test_list = My_DoublyLinkedList()
    assert my_test_list.list_is_empty() == True


def test_insert_ordered():
    global my_test_list
    my_test_list = My_DoublyLinkedList()
    my_test_list.insert_ordered(4)

    header_1 = my_test_list._get_header()
    tail_1 = my_test_list._get_tail()
    assert my_test_list._get_header() != None
    assert my_test_list._get_tail() != None

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == [4]
    my_test_list.insert_ordered(8)
    assert my_test_list._get_tail() != tail_1
    my_test_list.insert_ordered(2)
    assert my_test_list._get_header() != header_1
    my_test_list.insert_ordered(9)
    my_test_list.insert_ordered(1)

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == [1, 2, 4, 8, 9]


def test_remove_():
    global my_test_list
    my_test_list = My_DoublyLinkedList()

    my_test_list._remove_(1)                          #a

    my_test_list.insert_ordered(1)
    my_test_list.insert_ordered(2)
    my_test_list.insert_ordered(3)
    my_test_list.insert_ordered(4)
    my_test_list.insert_ordered(5)

    my_test_list._remove_(2)

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == [1, 3, 4, 5]                #b

    my_test_list._remove_(100)

    assert test_list == [1, 3, 4, 5]                #c

    my_test_list._remove_(1)
    my_test_list._remove_(3)
    my_test_list._remove_(4)
    my_test_list._remove_(5)

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == []
    assert my_test_list._get_header() == None

    my_test_list.insert_ordered(1)
    my_test_list.insert_ordered(2)
    my_test_list.insert_ordered(3)

    header_1 = my_test_list._get_header()

    my_test_list._remove_(1)

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == [2, 3]
    assert my_test_list._get_header() != header_1      #e

    my_test_list._remove_(3)
    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == [2]

def test_remove_duplicates():
    global my_test_list
    my_test_list = My_DoublyLinkedList()

    my_test_list.insert_ordered(1)
    my_test_list.insert_ordered(2)
    my_test_list.insert_ordered(3)
    my_test_list.insert_ordered(3)
    my_test_list.insert_ordered(4)

    my_test_list.remove_duplicates()

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == [1, 2, 3, 4]                #a

    my_test_list.insert_ordered(2)
    my_test_list.insert_ordered(2)

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)
    assert test_list == [1, 2, 2, 2, 3, 4]

    my_test_list.remove_duplicates()

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == [1, 2, 3, 4]                #b

    my_test_list.insert_ordered(1)
    my_test_list.insert_ordered(2)

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)
    assert test_list == [1, 1, 2, 2, 3, 4]

    my_test_list.remove_duplicates()

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == [1, 2, 3, 4]                #c

    my_test_list.insert_ordered(1)
    my_test_list.insert_ordered(1)
    my_test_list.insert_ordered(2)
    my_test_list.insert_ordered(3)
    my_test_list.insert_ordered(3)

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == [1, 1, 1, 2, 2, 3, 3, 3, 4]

    my_test_list.remove_duplicates()

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == [1, 2, 3, 4]                #d


def test_reorder_list():
    global my_test_list
    my_test_list = My_DoublyLinkedList()

    my_test_list.reorder_list()                     #a

    my_test_list.insert_in_empty_list(5)
    my_test_list.insert_at_end(3)
    my_test_list.insert_at_end(1)
    my_test_list.insert_at_end(9)
    my_test_list.insert_at_end(8)
    my_test_list.insert_at_end(4)
    my_test_list.insert_at_end(2)

    my_test_list.reorder_list()

    test_list = []
    for item in my_test_list.iter():
        test_list.append(item)

    assert test_list == [1, 3, 5, 9, 2, 4, 8]
    assert my_test_list.reorder_list() == 4         #b

    my_test_list2 = My_DoublyLinkedList()
    my_test_list2.insert_in_empty_list(4)
    my_test_list2.insert_at_end(2)
    my_test_list2.insert_at_end(8)
    my_test_list2.insert_at_end(6)

    my_test_list2.reorder_list()

    test_list = []
    for item in my_test_list2.iter():
        test_list.append(item)

    assert test_list == [2, 4, 6, 8]                  #c

    my_test_list3 = My_DoublyLinkedList()
    my_test_list3.insert_in_empty_list(7)
    my_test_list3.insert_at_end(5)
    my_test_list3.insert_at_end(3)
    my_test_list3.insert_at_end(11)
    my_test_list3.insert_at_end(1)

    assert my_test_list3.reorder_list() == -1

    test_list = []
    for item in my_test_list3.iter():
        test_list.append(item)

    assert test_list == [1, 3, 5, 7, 11]                 #d


def test_get_integer_value():
    global my_test_list
    my_test_list = My_DoublyLinkedList()

    my_test_list.get_integer_value(4)                    #a

    my_test_list.insert_ordered(1)
    my_test_list.insert_ordered(3)
    my_test_list.insert_ordered(4)
    my_test_list.insert_ordered(5)

    assert my_test_list.get_integer_value(0) == 1

    my_test_list.get_integer_value(5)                    #b