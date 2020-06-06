from MyHeapPriorityQueue import MyHeapPriorityQueue


def test_insert():
    queue = MyHeapPriorityQueue(init_capicity=4)
    assert queue.is_empty()

    queue.insert(1)
    assert queue.get_min() == 1
    queue.insert(2)
    assert queue.get_min() == 1
    queue.insert(3)
    queue.insert(4)
    assert queue.heap == [1, 2, 3, 4]
    assert queue.size == 4

    # Insert which requires resizing the internal array
    queue.insert(5)
    assert queue.heap == [1, 2, 3, 4, 5, None, None, None]
    assert queue.size == 5
    assert queue.get_size() == 5
    assert queue.get_min() == 1

    queue.insert(0)
    assert queue.heap == [0, 2, 1, 4, 5, 3, None, None]
    assert queue.get_min() == 0
    assert queue.get_size() == 6

    assert not queue.is_empty()


def test_remove():
    queue = MyHeapPriorityQueue(init_capicity=4)
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.insert(4)
    queue.insert(0)
    assert queue.heap == [0, 1, 3, 4, 2, None, None, None]
    queue.remove_min()
    assert queue.heap == [1, 2, 3, 4, None, None, None, None]
    queue.remove_min()
    assert queue.heap == [2, 4, 3, None, None, None, None, None]

    min_values = [2, 3, 4, None, None]
    for v in min_values:
        assert v == queue.remove_min()



