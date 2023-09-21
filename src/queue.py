class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        node.next_node = None
        if self.length == 0:
            self.head = self.tail = node  # голова и хвост равны
        else:
            tail = self.tail
            tail.next_node = node
            self.tail = node
        self.length += 1

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.length == 0:
            return
        head = self.head.data
        self.head = self.head.next_node
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return head

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        n = self.head
        result = []
        while n:
            result.append(n.data)
            n = n.next_node
        return "\n".join(result)
