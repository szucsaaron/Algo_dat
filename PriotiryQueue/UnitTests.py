import unittest

from MyLinkedList import MyLinkedList
from MyListPriorityQueue import MyListPriorityQueue


class UnitTests(unittest.TestCase):

    '''Test MyLinkedList'''

    def test_list_add_first(self):
        list = MyLinkedList()

        list.add_first(2)
        self.assertEqual(2, list.get_first())
        list.add_first(3)
        self.assertEqual(3, list.get_first())
        list.add_first(1)
        self.assertEqual(1, list.get_first())

        ex = None
        try:
            list.add_first(None)
        except ValueError as ve:
            ex = ve
        self.assertTrue(isinstance(ex, ValueError))

    def test_list_clear(self):
        list = MyLinkedList()

        list.add_last(2)
        list.add_first(3)
        list.add_last(1)
        list.add_first(8)

        self.assertEqual(4, list.get_size())

        list.clear()
        self.assertEqual(0, list.get_size())

    def test_list_contains(self):
        list = MyLinkedList()

        list.add_last(2)
        list.add_first(3)
        list.add_last(1)
        list.add_first(8)
        list.add_last(9)
        list.add_first(10)
        list.add_last(5)
        list.add_first(3)
        list.add_last(15)

        self.assertTrue(list.contains(2))
        self.assertTrue(list.contains(3))
        self.assertTrue(list.contains(1))
        self.assertTrue(list.contains(8))
        self.assertTrue(list.contains(9))
        self.assertTrue(list.contains(10))
        self.assertTrue(list.contains(15))
        self.assertTrue(list.contains(3))
        self.assertFalse(list.contains(0))
        self.assertFalse(list.contains(11))

        ex = None
        try:
            list.contains(None)
        except ValueError as ve:
            ex = ve
        self.assertTrue(isinstance(ex, ValueError))

    '''Test PQ'''

    def test_PQ_is_empty(self):
        pq = MyListPriorityQueue()
        self.assertTrue(pq.is_empty())

    def test_pq_min(self):
        pq = MyListPriorityQueue()
        pq.insert(20)
        self.assertEqual(20, pq.get_min())
        pq.insert(21)
        self.assertEqual(20, pq.get_min())
        pq.insert(2)
        self.assertEqual(2, pq.get_min())
        pq.insert(3)
        self.assertEqual(2, pq.get_min())
        pq.remove_min()
        self.assertEqual(3, pq.get_min())

    def test_pq_to_list(self):
        pq = MyListPriorityQueue()
        pq.insert(2)
        pq.insert(3)
        pq.insert(1)
        pq.insert(8)
        pq.insert(19)

        a = pq.to_list()
        self.assertEqual(pq.get_min(), a[0])
        self.assertEqual(pq.get_size(), len(a))
