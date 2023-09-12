"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack

class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack()
        self.assertIsNone(stack.push('data1'))
        self.assertEqual(stack.pop(), 'data1')


    def test_node(self):

        self.assertTrue(Node(3))


if __name__ == '__main__':
    unittest.main()