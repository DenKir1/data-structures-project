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


if __name__ == '__main__':
    unittest.main()
