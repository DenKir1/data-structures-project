"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestStack(unittest.TestCase):

    def test_queue(self):
        que = Queue()
        que.enqueue('data1')
        que.enqueue('data2')
        self.assertIsNone(que.enqueue('data3'))
        self.assertEqual(que.dequeue(), 'data1')
        self.assertEqual(que.dequeue(), 'data2')
        self.assertEqual(que.dequeue(), 'data3')
        self.assertEqual(que.dequeue(), None)

    def test_node(self):
        self.assertTrue(Node(3))

    def test_str(self):
        que = Queue()
        que.enqueue('data1')
        que.enqueue('data2')

        self.assertEqual(str(que), 'data1\ndata2')


if __name__ == '__main__':
    unittest.main()
