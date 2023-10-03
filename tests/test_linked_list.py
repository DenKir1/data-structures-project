"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class TestStack(unittest.TestCase):

    def test_node(self):
        self.assertTrue(Node(3))

    def test_str_and_etc(self):
        lli = LinkedList()
        lli.insert_beginning({'data2': 2})
        lli.insert_beginning({'data1': 1})
        lli.insert_at_end({'data3': 3})

        self.assertEqual(str(lli), "{'data1': 1} -> {'data2': 2} -> {'data3': 3} -> None")

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        lst = ll.to_list()
        self.assertEqual(lst, [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}])

    def test_get_data(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        user_data = ll.get_data_by_id(2)
        self.assertEqual(user_data, {'id': 2, 'username': 'mik.roz'})


if __name__ == '__main__':
    unittest.main()
